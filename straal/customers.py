from dataclasses import dataclass, field
from typing import List, Optional

from straal.base import ApiObject


@dataclass
class Customer(ApiObject):
    RESOURCE_CREATE_URI = "/v1/customers"
    RESOURCE_DETAIL_URI = "/v1/customers/{idx}"
    RESOURCE_LIST_URI = "/v1/customers"
    id: str
    created_at: int
    email: str
    reference: str
    last_transaction: Optional[dict] = field(default=None, repr=False)

    @classmethod
    def create(cls, email: str, reference: str) -> "Customer":
        return super().create(email=email, reference=reference)

    @classmethod
    def get(cls, id: str) -> "Customer":
        return super().get(idx=id)

    @classmethod
    def list(cls) -> List["Customer"]:
        return super().list()
