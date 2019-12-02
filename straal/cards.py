from dataclasses import dataclass, field

from straal.base import ApiObject


@dataclass
class Card(ApiObject):
    RESOURCE_CREATE_URI = "/v1/customers/{customer_id}/cards"
    RESOURCE_DETAIL_URI = "/v1/cards/{idx}"
    RESOURCE_LIST_URI = "/v1/cards"
    id: str
    created_at: int
    state: str
    brand: str
    name: str
    num_bin: str
    num_last_4: str
    expiry_month: int
    expiry_year: int
    origin_ipaddr: str
    customer: dict = field(repr=False)
    extra_data: dict = field(repr=False)
    state_flags: list = field(repr=False)
    transactions: list = field(default=None, repr=False)

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

    @classmethod
    def get(cls, id: str) -> "Card":
        return super().get(idx=id)
