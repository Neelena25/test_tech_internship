import pytest
import requests


@pytest.mark.parametrize("body, missing_field", [
    ({"name": "Test", "price": 100, "statistics": {"likes": 1, "viewCount": 1, "contacts": 1}}, "sellerID"),
    ({"sellerID": 123, "price": 100, "statistics": {"likes": 1, "viewCount": 1, "contacts": 1}}, "name"),
    ({"sellerID": 123, "name": "Test", "statistics": {"likes": 1, "viewCount": 1, "contacts": 1}}, "price"),
    ({"sellerID": 123, "name": "Test", "price": 100}, "statistics"),
])
def test_post_required_fields(base_url, body, missing_field):
    r = requests.post(f"{base_url}/api/1/item", json=body)

    assert r.status_code == 400