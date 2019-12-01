from abc import ABC
from typing import List, TypeVar, Type
from urllib.parse import urljoin

import requests

from straal import API_KEY, BASE_URL

T = TypeVar("T", bound="ApiObject")


class ApiObject(ABC):
    RESOURCE_URI: str

    @classmethod
    def create(cls: Type[T], **kwargs) -> T:
        req_url = urljoin(BASE_URL, cls.RESOURCE_URI)
        res = requests.post(req_url, json=kwargs, auth=("", API_KEY))
        return cls(**res.json())

    @classmethod
    def get(cls: Type[T], idx: str) -> T:
        resource_url = urljoin(BASE_URL, cls.RESOURCE_URI)
        req_url = f"{resource_url}/{idx}"
        res = requests.get(req_url, auth=("", API_KEY))
        return cls(**res.json())

    @classmethod
    def list(cls: Type[T]) -> List[T]:
        req_url = urljoin(BASE_URL, cls.RESOURCE_URI)
        res = requests.get(req_url, auth=("", API_KEY))
        return [cls(**entry) for entry in res.json()["data"]]
