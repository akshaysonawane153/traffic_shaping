import pytest
from app.api_client import TrafficAPIClient


@pytest.fixture
def api():
    client = TrafficAPIClient("http://127.0.0.1:8000")
    return client

def test_get_all_records(api):
    resp = api.get_records()
    print(resp.json())
    assert resp.status_code == 200

def test_health_check(api):
    resp = api.get_health_status()
    print(resp.json())
    assert resp.status_code == 200