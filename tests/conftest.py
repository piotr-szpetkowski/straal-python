import pytest


@pytest.fixture(scope="session")
def straal_base_url():
    return "https://straal/"


@pytest.fixture(autouse=True, scope="function")
def env_test_setup(monkeypatch, straal_base_url):
    """
    Makes sure tests will never fire requests to actual server
    """
    import straal

    straal.init("DUMMY_TEST_API_KEY", straal_base_url)


@pytest.fixture(scope="session")
def customer_json():
    return {
        "id": "xyz_123",
        "created_at": 1575376785,
        "email": "customer@example.net",
        "reference": "SOME_ID",
    }
