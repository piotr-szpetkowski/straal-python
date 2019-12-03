from abc import ABC
from string import Formatter
from typing import List, Type, TypeVar
from urllib.parse import urljoin

import requests

from straal import API_KEY, BASE_URL

T = TypeVar("T", bound="ApiObject")


def _get_required_format_vars(url: str) -> List[str]:
    return [ref for _, ref, _, _ in Formatter().parse(url) if ref is not None]


def _build_request_data(uri: str, **kwargs):
    req_url_tpl = urljoin(BASE_URL, uri)
    required_format_vars = _get_required_format_vars(req_url_tpl)
    # TODO: Provide better exc with proper ctx instead of KeyError
    format_kwargs = {k: kwargs[k] for k in required_format_vars}
    for kwarg in required_format_vars:
        kwargs.pop(kwarg)

    return req_url_tpl.format(**format_kwargs), kwargs


class ApiObject(ABC):
    RESOURCE_CREATE_URI: str
    RESOURCE_DETAIL_URI: str
    RESOURCE_LIST_URI: str

    @classmethod
    def create(cls: Type[T], **kwargs) -> T:
        req_url, json_data = _build_request_data(cls.RESOURCE_CREATE_URI, **kwargs)
        res = requests.post(req_url, json=json_data, auth=("", API_KEY))
        return cls(**res.json())

    @classmethod
    def get(cls: Type[T], **kwargs) -> T:
        req_url, _ = _build_request_data(cls.RESOURCE_DETAIL_URI, **kwargs)
        res = requests.get(req_url, auth=("", API_KEY))
        return cls(**res.json())

    @classmethod
    def list(cls: Type[T], **kwargs) -> List[T]:
        req_url, _ = _build_request_data(cls.RESOURCE_LIST_URI, **kwargs)
        res = requests.get(req_url, auth=("", API_KEY))
        return [cls(**entry) for entry in res.json()["data"]]
