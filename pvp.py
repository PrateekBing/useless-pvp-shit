import flask
from flask import request, redirect, url_for
import mysql.connector as cn
import time

app = flask.Flask(__name__)

lb = []

mydb = cn.connect(
    host = 'IsolatedSoul.mysql.pythonanywhere-services.com'
    user = 'IsolatedSoul'
    passwd = 'uselesspvpshit'
    database = 'IsolatedSoul$default'
)

a = b = None
@app.route("/")
def index():
    return "Hello there"

@app.route("/ajudge", methods = ["POST"])
def ajudge():
    data = request.get_json()
    global a
    a = int(data['score'])
    return redirect(url_for("result"))

@app.route("/bjudge", methods = ["POST"])
def bjudge():
    data = request.get_json()
    global b
    b =  int(data["score"])
    return redirect(url_for("result"))

@app.route("/result", methods = ["POST"])
def result():
    d = 0
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
    
@app.route("/leaderboard")
def leaderboard():
    return lb

if __name__ == "__main__":
    app.run()