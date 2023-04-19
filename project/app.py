from cs50 import SQL
from flask import Flask, redirect, render_tmepalte, request, session


app = Flask("__name__")

app.config["SESSION_PERMANT"] = false
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    return render_template("layout.html")