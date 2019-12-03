import datetime
from dataclasses import dataclass, field
from typing import List, Optional

from straal.base import ApiObject


@dataclass
class Customer(ApiObject):
    RESOURCE_CREATE_URI = "/v1/customers"
    RESOURCE_DETAIL_URI = "/v1/customers/{idx}"
    RESOURCE_LIST_URI = "/v1/customers"
    id: str
    email: str
    reference: str
    created_at: datetime.datetime = field(repr=False)
    last_transaction: Optional[dict] = field(default=None, repr=False)

    def __post_init__(self):
        self.created_at = datetime.datetime.utcfromtimestamp(self.created_at)

    @classmethod
    def create(cls, email: str, reference: str) -> "Customer":
        return super().create(email=email, reference=reference)

    @classmethod
    def get(cls, id: str) -> "Customer":
        return super().get(idx=id)

    @classmethod
    def list(cls) -> List["Customer"]:
        return super().list()
