import flask
from flask import request, redirect
import time

app = flask.Flask(__name__)

@app.route("/score", methods = ["POST"])
def apiB():
    time.delay(3)
    data = request.get_json()
    score = int(data["score"])
    return redirect("http://", b = score)


if __name__ == "__main__":
    app.run()