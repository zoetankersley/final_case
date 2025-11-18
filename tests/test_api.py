from src.app import app

def test_health():
    client = app.test_client()
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json.get("status") == "ok"

def test_quote_default():
    client = app.test_client()
    resp = client.get("/quote")
    assert resp.status_code == 200
    assert "quote" in resp.json

def test_quote_category():
    client = app.test_client()
    resp = client.get("/quote?category=productivity")
    assert resp.status_code == 200
    assert "quote" in resp.json

