import requests

def test_post_success(base_url):
    body = {
    }

    r = requests.post(f"{base_url}/api/1/item", json=body)

    assert r.status_code == 400