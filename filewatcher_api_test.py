import flask

import filewatcher_api

client = filewatcher_api.app.test_client()


def test_hashing():
    with open("a.txt", "w") as file:
        file.write("hello")

    res: flask.Response = client.get("/api/hash?directory=.")

    assert res.status_code == 200

    assert len(res.json.keys()) == 1
    assert res.json["a.txt"] == "5d41402abc4b2a76b9719d911017c592"


def test_verify_success():
    with open("a.txt", "w") as file:
        file.write("hello")

    res: flask.Response = client.post(
        "/api/verify?directory=.", json={"a.txt": "5d41402abc4b2a76b9719d911017c592"}
    )

    assert res.status_code == 200

    assert len(res.json.keys()) == 1
    assert res.json["result"] == "success"


def test_verify_failure():
    res: flask.Response = client.post(
        "/api/verify?directory=.", json={"a.txt": "5d41402abc4b2a76b9719d911017c592"}
    )

    with open("a.txt", "w") as file:
        file.write("hello")

    assert res.status_code == 200

    assert len(res.json.keys()) == 1
    assert res.json["result"] == "failure"
