from flask import Flask, jsonify
from appcfg import TEST, TEST_ACTION


def create_app(test_config=None):
    app = Flask(__name__)

    if test_config is None:
        print("no config")
        app.config.from_pyfile("appcfg.py", silent=True)
    else:
        print("test config")

    @app.route("/")
    def hello_world():  # put application's code here
        return jsonify(TEST)

    @app.route("/test")
    def test_action():
        return jsonify(TEST_ACTION)

    return app
