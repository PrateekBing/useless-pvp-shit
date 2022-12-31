import flask
import time

app = flask.Flask(__name__)

a = b = None
lb = []

@app.get("/")
def home():
    return "Hello there!"


@app.post("/ajudge")
def ajudge(name, score):
    a = score
    naam = name
    lb.append([naam, a])

@app.post("/bjudge")
def bjudge(name, score):
    b = score
    naam = name
    lb.append([naam, b])


@app.get("/result")
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


@app.get("/leaderboard")
def leaderboard():
    return lb

if __name__ == "__main__":
    app.run()