import requests

def test_get_items(base_url):
    r = requests.get(f"{base_url}/api/1/488283/item")
    assert r.status_code == 200
    assert isinstance(r.json(), list)