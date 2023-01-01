import flask
import flask
from flask import request
import requests

app = flask.Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def result(b):
    a = int(requests.get("http://"))
    global winner
    if a > b:
        winner = "a"
    else:
        winner =  "b"
    return

@app.route("/winner", methods = ["GET"])
def winner():
    return winner



if __name__ == "__main__":
    app.run()
