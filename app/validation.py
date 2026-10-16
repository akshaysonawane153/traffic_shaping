def validate_traffic(data):
    try:
        throughput_mbps = float(data["throughput_mbps"])
        latency_ms = float(data["latency_ms"])
        packet_loss_pct = float(data["packet_loss_pct"])
    except (KeyError, ValueError, TypeError, OverflowError) as e:
        raise ValueError(f"Exception occurred while parsing data at - {e}") from e

    if throughput_mbps <= 0 or latency_ms < 0 or not (0<= packet_loss_pct <= 100):
        return False
    return True
