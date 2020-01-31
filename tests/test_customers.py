import datetime
import json

import responses

import straal


@responses.activate
def test_customer_create_success(straal_base_url, customer_json):
    url = fr"{straal_base_url}v1/customers"
    responses.add(responses.POST, url, json=customer_json)

    customer = straal.Customer.create(
        email=customer_json["email"], reference=customer_json["reference"]
    )

    assert len(responses.calls) == 1
    straal_request = json.loads(responses.calls[0].request.body)
    assert straal_request == {
        "email": customer_json["email"],
        "reference": customer_json["reference"],
    }

    assert customer.id == customer_json["id"]
    assert customer.email == customer_json["email"]
    assert customer.reference == customer_json["reference"]
    created_at = datetime.datetime.utcfromtimestamp(customer_json["created_at"])
    assert customer.created_at == created_at
    assert customer.last_transaction is None


@responses.activate
def test_customer_create_without_reference_success(straal_base_url, customer_json):
    customer_json["reference"] = None
    url = fr"{straal_base_url}v1/customers"
    responses.add(responses.POST, url, json=customer_json)

    customer = straal.Customer.create(email=customer_json["email"])

    assert len(responses.calls) == 1
    straal_request = json.loads(responses.calls[0].request.body)
    assert straal_request == {"email": customer_json["email"]}

    assert customer.id == customer_json["id"]
    assert customer.email == customer_json["email"]
    assert customer.reference is None
    created_at = datetime.datetime.utcfromtimestamp(customer_json["created_at"])
    assert customer.created_at == created_at
    assert customer.last_transaction is None


@responses.activate
def test_existing_customer_get_success(straal_base_url, customer_json):
    url = fr"{straal_base_url}v1/customers/{customer_json['id']}"
    responses.add(responses.GET, url, json=customer_json)

    customer = straal.Customer.get(customer_json["id"])

    assert len(responses.calls) == 1
    straal_request = responses.calls[0].request
    assert straal_request.body is None

    assert customer.id == customer_json["id"]
    assert customer.email == customer_json["email"]
    assert customer.reference == customer_json["reference"]
    created_at = datetime.datetime.utcfromtimestamp(customer_json["created_at"])
    assert customer.created_at == created_at
    assert customer.last_transaction is None


@responses.activate
def test_list_customers_success(straal_base_url, customer_list_json):
    url = fr"{straal_base_url}v1/customers"
    responses.add(responses.GET, url, json=customer_list_json)

    customer_list = straal.Customer.list()

    assert len(responses.calls) == 1
    straal_request = responses.calls[0].request
    assert straal_request.body is None

    assert isinstance(customer_list, list)
    assert len(customer_list) == 2

    assert customer_list[0].id == customer_list_json["data"][0]["id"]
    assert customer_list[0].email == customer_list_json["data"][0]["email"]
    assert customer_list[0].reference == customer_list_json["data"][0]["reference"]
    created_at_ts = customer_list_json["data"][0]["created_at"]
    created_at = datetime.datetime.utcfromtimestamp(created_at_ts)
    assert customer_list[0].created_at == created_at
    assert customer_list[0].last_transaction is None

    assert customer_list[1].id == customer_list_json["data"][1]["id"]
    assert customer_list[1].email == customer_list_json["data"][1]["email"]
    assert customer_list[1].reference == customer_list_json["data"][1]["reference"]
    created_at_ts = customer_list_json["data"][1]["created_at"]
    created_at = datetime.datetime.utcfromtimestamp(created_at_ts)
    assert customer_list[1].created_at == created_at
    assert customer_list[1].last_transaction is None
