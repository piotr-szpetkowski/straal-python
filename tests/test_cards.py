import datetime
import json

import responses

import straal
from straal.cards import CardBrand, CardState


@responses.activate
def test_card_create_for_customer_success(straal_base_url, visa_card_json):
    customer_id = visa_card_json["customer"]["id"]
    url = fr"{straal_base_url}v1/customers/{customer_id}/cards"
    responses.add(responses.POST, url, json=visa_card_json)

    card = straal.Card.create(
        customer_id=customer_id,
        name=visa_card_json["name"],
        number="4444444444444448",
        cvv="123",
        expiry_month=visa_card_json["expiry_month"],
        expiry_year=visa_card_json["expiry_year"],
        origin_ipaddr=visa_card_json["origin_ipaddr"],
    )

    assert len(responses.calls) == 1
    straal_request = json.loads(responses.calls[0].request.body)
    assert straal_request == {
        "name": visa_card_json["name"],
        "number": "4444444444444448",
        "cvv": "123",
        "expiry_year": visa_card_json["expiry_year"],
        "expiry_month": visa_card_json["expiry_month"],
        "origin_ipaddr": visa_card_json["origin_ipaddr"],
    }

    assert card.id == visa_card_json["id"]
    assert card.name == visa_card_json["name"]
    assert card.num_bin == visa_card_json["num_bin"]
    assert card.num_last_4 == visa_card_json["num_last_4"]
    assert card.expiry_month == visa_card_json["expiry_month"]
    assert card.expiry_year == visa_card_json["expiry_year"]
    assert card.origin_ipaddr == visa_card_json["origin_ipaddr"]
    assert card.brand == CardBrand.VISA
    assert card.state == CardState.ACTIVE
    created_at = datetime.datetime.utcfromtimestamp(visa_card_json["created_at"])
    assert card.created_at == created_at
    assert card.customer == visa_card_json["customer"]
    assert card.extra_data == {}
    assert card.straal_custom_data == {}
    assert card.state_flags == []
    assert card.transactions == []
    assert card.is_active is True
