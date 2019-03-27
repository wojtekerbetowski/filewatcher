import flask

import filewatcher_web

client = filewatcher_web.app.test_client()


def test_hashing():
    with open("a.txt", "w") as file:
        file.write("hello")

    res: flask.Response = client.get("/web/hash?directory=.")

    assert res.status_code == 200, res.data

    assert b"a.txt" in res.data
