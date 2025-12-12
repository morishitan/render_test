from app import app

def test_health():
    app.config["TESTING"] = True
    with app.test_client() as c:
        r = c.get("/health")
        assert r.status_code == 404
        assert r.get_json()["status"] == "ok"
