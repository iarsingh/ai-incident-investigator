from fastapi.testclient import TestClient
from incinv.main import app

client = TestClient(app)


def test_runs_and_refuses_a_write():
    payload = client.post("/agent/run", json={"goal": 'investigate the 5xx spike', **{'payload': {'facts': ['rollout of api-2.0 at 18:01']}}}).json()
    assert payload["refused"] is False
    assert payload["applied"] is False
    assert payload["hypothesis"] == "bad_deploy"
    refused = client.post("/agent/run", json={"goal": 'page secondary now'}).json()
    assert refused["refused"] is True
