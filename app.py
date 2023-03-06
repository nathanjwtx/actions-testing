from flask import Flask, jsonify
from appcfg import TEST


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is None:
        app.config.from_pyfile("appcfg.py", silent=True)

    @app.route("/")
    def hello_world():  # put application's code here
        return jsonify(TEST)

    return app
