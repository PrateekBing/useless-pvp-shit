import flask
import time

app = flask.Flask(__name__)

a = b = None
lb = []

@app.route("/")
def index():
    return "pvp"

@app.route("/ajudge", methods = ["POST"])
def ajudge(score):
    return score

@app.route("/bjudge", methods = ["POST"])
def bjudge(score):
    b = score
    return b


@app.route("/result")
def result():
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
    app.run()