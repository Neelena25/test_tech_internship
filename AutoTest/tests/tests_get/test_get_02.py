import requests

def test_get_items(base_url):
    r = requests.get(f"{base_url}/api/1/rr/item")
    assert r.status_code == 400
    assert isinstance(r.json(), dict)