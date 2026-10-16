import pytest

from app.validation import validate_traffic

@pytest.fixture
def valid_record():
    return {
        "record_id": "TR-1001",
        "protocol": "TCP",
        "throughput_mbps": 82.5,
        "latency_ms": 24,
        "packet_loss_pct": 0.1
    }

def test_all_traffic_parameters(valid_record):
    assert validate_traffic(valid_record) is True


def test_negative_latency_ms(valid_record):
    valid_record["latency_ms"] = -2
    assert validate_traffic(valid_record) is False

def test_packet_loss_above_100(valid_record):
    valid_record["packet_loss_pct"] = 105

