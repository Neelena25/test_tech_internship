import requests

def test_delete_item(base_url):
    # Находила item_id в Postman. Статус кода не соответствует TESTCASES.md
    item_id = "c6815627-f498-4639-a77b-320f6cdb11d9"
    r = requests.delete(f"{base_url}/api/2/item/{item_id}")
    assert r.status_code == 404