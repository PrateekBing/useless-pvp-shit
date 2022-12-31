import flask
import flask
from flask import request
import requests

app = flask.Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def result(b):
    a = int(requests.get("http://"))
    
    if a > b:
        return "a"
    else:
        return "b"



if __name__ == "__main__":
    app.run()
