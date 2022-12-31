import flask
from flask import request, redirect, url_for
import mysql.connector as cn
import time

app = flask.Flask(__name__)

lb = []

mydb = cn.connect(
    host = 'IsolatedSoul.mysql.pythonanywhere-services.com',
    user = 'IsolatedSoul',
    passwd = 'uselesspvpshit',
    database = 'IsolatedSoul$default'
)

cursor = mydb.cursor()

a = b = None
@app.route("/")
def index():
    return "Hello there"

@app.route("/ajudge", methods = ["POST"])
def ajudge():
    data = request.get_json()
    global a
    a = int(data['score'])
    global num
    num = cursor.execute("select No from score order by no desc limit 1")
    cursor.execute("insert into score(No, A) values (%s, %s)", (num[0] + 1, a))
    cursor.commit()
    return

@app.route("/bjudge", methods = ["POST"])
def bjudge():
    time.sleep(3)
    data = request.get_json()
    global b
    b =  int(data["score"])
    cursor.execute("insert into score (B) values (%s) where No = %s", (b, num))
    cursor.commit()
    return redirect(url_for("result"))

@app.route("/result", methods = ["GET"])
def result():
    num = cursor.execute("select No from score order by no desc limit 1")
    P1 = int(cursor.execute("select A from score where No = %s", (num[0])))
    P2 = int(cursor.execute("select B from score where No = %s", (num[0])))
    cursor.commit()
    if P1 > P2:
        return "a"
    elif P2 < P1:
        return "b"
    else:
        return "d"

if __name__ == "__main__":
    app.run()