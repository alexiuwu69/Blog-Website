from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    name = ""
    if request.method == "POST":
        name = request.form["name"]
    print(name)
    return render_template("login.html")


if __name__ == "__main__":
    app.run("127.0.0.1", 9090, debug=True)