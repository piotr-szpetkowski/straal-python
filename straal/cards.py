from dataclasses import dataclass

from straal.base import ApiObject
from straal.customers import Customer


@dataclass
class Card(ApiObject):
    RESOURCE_CREATE_URI = "/v1/customers/{customer_id}/cards"
    RESOURCE_DETAIL_URI = "/v1/cards/{idx}"
    RESOURCE_LIST_URI = "/v1/cards"

    @classmethod
    def create(
        cls,
        customer_id: str,
        name: str,
        number: str,
        cvv: str,
        expiry_year: int,
        expiry_month: int,
        origin_ipaddr: str,
    ) -> "Card":
        return super().create(
            customer_id=customer_id,
            name=name,
            number=number,
            cvv=cvv,
            expiry_year=expiry_year,
            expiry_month=expiry_month,
            origin_ipaddr=origin_ipaddr,
        )
