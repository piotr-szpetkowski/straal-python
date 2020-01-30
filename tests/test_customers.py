import datetime

import responses

import straal


@responses.activate
def test_existing_customer_get_success(straal_base_url, customer_json):
    url = fr"{straal_base_url}v1/customers/{customer_json['id']}"
    responses.add(responses.GET, url, json=customer_json)

    customer = straal.Customer.get(customer_json["id"])
    assert customer.id == customer_json["id"]
    assert customer.email == customer_json["email"]
    assert customer.reference == customer_json["reference"]
    created_at = datetime.datetime.utcfromtimestamp(customer_json["created_at"])
    assert customer.created_at == created_at
    assert customer.last_transaction is None
