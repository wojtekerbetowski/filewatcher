import flask

from filewatcher import filewatcher

app = flask.Flask(__name__)


@app.route("/api/hash")
def hash_site():
    directory = flask.request.args["directory"]

    hash_tree = filewatcher.hash_tree(directory)

    return flask.jsonify(hash_tree)


@app.route("/api/verify", methods=["POST"])
def verify_site():
    directory = flask.request.args["directory"]

    hashes_to_verify = {}
    for path, hash in flask.request.json.items():
        hashes_to_verify[path] = hash

    hash_tree = filewatcher.hash_tree(directory)

    if hash_tree == hashes_to_verify:
        message = "success"
    else:
        message = "failure"

    return flask.jsonify(result=message)


if __name__ == "__main__":
    app.run(debug=True)
