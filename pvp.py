import flask
from flask import request, redirect, url_for
import time

app = flask.Flask(__name__)

a = b = None
lb = []

@app.route("/")
def index():
    return "Hello there"

@app.route("/ajudge", methods = ["POST"])
def ajudge():
        #data = request.get_json()
        ahere = 2
        bhere = 1
        return redirect(url_for("result"))

@app.route("/bjudge", methods = ["POST"])
def bjudge():
    data = request.get_json()
    b =  int(data["score"])
    return

@app.route("/result", methods = ["POST"])
def result():
    a = 1
    b = 2
    d = 0
    try:
        while d<3:
            if a != None and b != None:
                if a > b:
                    return "a"
                elif a < b:
                    return "b"
            else:
                time.sleep(1)
                d+=1
        return "0"
    except:
        return "0"

@app.route("/leaderboard")
def leaderboard():
    return lb

if __name__ == "__main__":
    app.run(debug = True)