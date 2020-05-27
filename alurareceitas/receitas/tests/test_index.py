def test_status_code(client, db):
    resp = client.get('/')
    assert resp.status_code == 200
