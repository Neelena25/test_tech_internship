import requests

def test_get_statistics(base_url):
    item_id = "25c4a7ed-c175-4c04-96f1-372faf899f0d2dgwfvewefefw"
    r = requests.get(f"{base_url}/api/1/statistic/{item_id}")
    assert r.status_code == 400