import flask

from filewatcher import filewatcher

app = flask.Flask(__name__)


@app.route('/web/hash')
def hash_site():
    directory = flask.request.args['directory']

    hash_tree = filewatcher.hash_tree(directory)


    return flask.render_template('hashes.html', hash_tree=hash_tree)


if __name__ == '__main__':
    app.run(debug=True)
