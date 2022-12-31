import flask
from flask import request, redirect, url_for
import mysql.connector as cn
import time
from flask_sqlalchemy import SQLAlchemy
import sshtunnel

app = flask.Flask(__name__)

lb = []

tunnel = sshtunnel.SSHTunnelForwarder(
    ('ssh.pythonanywhere.com'), ssh_username='IsolatedSoul', ssh_password='uselesspvpshit',
    remote_bind_address =('IsolatedSoul.mysql.pythonanywhere-services.com', 3306)
)

tunnel.start()

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://IsolatedSoul:uselesspvpshit@127.0.0.1:{}/IsolatedSoul$default'.format(tunnel.local_bind_port)

# mydb = cn.connect(
#     host = 'IsolatedSoul.mysql.pythonanywhere-services.com',
#     user = 'IsolatedSoul',
#     passwd = 'uselesspvpshit',
#     database = 'IsolatedSoul$default'
# )

mydb = SQLAlchemy(app)

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
    with mydb.commit() as conn:
        num = conn.execute("select No from score order by no desc limit 1")
        conn.execute("insert into score(No, A) values (%s, %s)", (num[0] + 1, a))
        conn.commit()
    return

@app.route("/bjudge", methods = ["POST"])
def bjudge():
    time.sleep(3)
    data = request.get_json()
    global b

    with mydb.commit() as conn:
        b = int(data['score'])
        conn.execute("insert into score(B) values (%s) where No = %s", (b, num[0]+1))
        conn.commit()

    # b =  int(data["score"])
    # cursor.execute("insert into score (B) values (%s) where No = %s", (b, num))
    # cursor.commit()
    return redirect(url_for("result"))

@app.route("/result", methods = ["POST","GET"])
def result():
    if request.method == "POST":
        with mydb.commit() as conn:
            num = conn.execute("select No from score order by no desc limit 1")
            P1 = int(conn.execute("select A from score where No = %s", (num[0])))
            P2 = int(conn.execute("select B from score where No = %s", (num[0])))
            conn.commit()

        if P1 > P2:
            return "a"
        elif P2 < P1:
            return "b"
        else:
            return "d"
    else:
        return "GET Call"

if __name__ == "__main__":
    app.run()