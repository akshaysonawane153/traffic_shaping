from fastapi import FastAPI

app = FastAPI(title="Traffic Shaping api")

TRAFFIC_RECORDS = [
    {
        "record_id": "TR-1001",
        "protocol": "TCP",
        "throughput_mbps": 82.5,
        "latency_ms": 24.0,
        "packet_loss_pct": 0.1
    },
    {
        "record_id": "TR-1002",
        "protocol": "UDP",
        "throughput_mbps": 95.0,
        "latency_ms": 18.5,
        "packet_loss_pct": 0.3
    }
]


@app.get("/api/health_status")
def health_status():
    return {"status": "OK"}

@app.get("/api/get_all_records")
def get_records():
    return TRAFFIC_RECORDS

@app.get("/api/total_records")
def total_records():
    return len(TRAFFIC_RECORDS)