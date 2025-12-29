import requests

def test_post_success(base_url):
    body = {
        "sellerID": 488283,
        "name": "Seller_10",
        "price": 700,
        "statistics": {"likes": 6, "viewCount": 14, "contacts": 4}
    }

    r = requests.post(f"{base_url}/api/1/item", json=body)

    assert r.status_code == 200