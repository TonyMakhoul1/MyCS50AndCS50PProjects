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

@app.route("/login")
def login():
    session.clear()

    if method == "GET":
        return render_template("login.html")
    
