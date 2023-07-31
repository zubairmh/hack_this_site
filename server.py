from flask import Flask, render_template, request

global comments
comments = []

global counter
counter=0
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/injection")
def injection():
    return render_template("injection.html", comments=comments)

@app.route("/comment")
def comment():
    global comments
    comments.append("X")
    return "OK"

@app.route("/ddos")
def ddos():
    global counter
    counter+=1
    return render_template("ddos.html", count=counter)

@app.route("/calculate")
def calculate():
    number = int(request.args.get("number"))
    power = int(request.args.get("power"))
    return f"Power is: {number**power}"


app.run(host="0.0.0.0", debug=True)
