from flask import Flask
from appcfg import TEST

app = Flask(__name__)


@app.route("/")
def hello_world():  # put application's code here
    return TEST


if __name__ == "__main__":
    app.run()
