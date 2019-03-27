import flask

import filewatcher_web

client = filewatcher_web.app.test_client()


def test_hashing():
    with open("a.txt", "w") as file:
        file.write("hello")

    res: flask.Response = client.get("/web/hash?directory=.")

    assert res.status_code == 200, res.data

    assert b"a.txt" in res.data


def test_verify_success():
    with open("a.txt", "w") as file:
        file.write("hello")

    res: flask.Response = client.post(
        "/web/verify",
        data={"hashes": "a.txt=5d41402abc4b2a76b9719d911017c592", "directory": "."},
    )
    body = res.data.decode()

    assert res.status_code == 200

    assert "Verification passed" in body


def test_verify_failure():
    res: flask.Response = client.post(
        "/web/verify",
        data={"hashes": "a.txt=5d41402abc4b2a76b9719d911017c592", "directory": "."},
    )
    body = res.data.decode()

    assert res.status_code == 200

    assert "Verification failed" in body
