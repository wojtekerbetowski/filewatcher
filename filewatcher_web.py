import flask

from filewatcher import filewatcher

app = flask.Flask(__name__)


@app.route("/web/hash")
def hash_site():
    directory = flask.request.args["directory"]

    hash_tree = filewatcher.hash_tree(directory)

    return flask.render_template("hashes.html", hash_tree=hash_tree)


@app.route("/web/verify", methods=["GET", "POST"])
def verify_site():
    if flask.request.method == "GET":
        return flask.render_template("verify_form.html")

    directory = flask.request.form["directory"]

    hashes_to_verify = {}
    for item in flask.request.form["hashes"].split("\r\n"):
        path, hash = item.split("=")
        hashes_to_verify[path] = hash

    hash_tree = filewatcher.hash_tree(directory)

    if hash_tree == hashes_to_verify:
        message = "Verification passed"
    else:
        message = "Verification failed"

    return flask.render_template("verify.html", message=message)


if __name__ == "__main__":
    app.run(debug=True)
