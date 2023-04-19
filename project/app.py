from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session

app = Flask("__name__")

app.config["SESSION_PERMANT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///project.db")

@app.route("/")
def index():
    return render_template("layout.html")

@app.route("/login", methods=['GET','POST'])
def login():
    session.clear()

    if request.method == "GET":
        return render_template("login.html")

@app.route("/register", methods=['GET','POST'])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        confirmpassword = request.form.get("confirmpassword")

        if not username:
            message = "You should Give A Username"
            return render_template("message.html", message = message)
        if not password:
            message = "You Should Give A Password"
            return render_template("message.html", message = message)
        if not confirmpassword:
            message = "You Should Do The Confirmation"
            return render_template("message.html", message = message)


