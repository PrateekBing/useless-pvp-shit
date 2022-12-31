import flask
from flask import request

app = flask.Flask(__name__)

@app.route("/score", methods = ["GET", "POST"])
def apiA():
    if flask.request.method == "POST":
        data = request.get_json()
        score = int(data["score"])
        return score
    else:
        return "a"

if __name__ == "__main__":
    app.run()