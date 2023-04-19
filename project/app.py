from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

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
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        if not username:
            message1 = "Enter A Username"
            return render_template("message.html", message = message1)
        elif not password:
            message2 = "Enter A Password"
            return render_template("message.html", message = message2)

        user = db.execute("SELECT * FROM users WHERE username = ?", username)

        if user and check_password_hash(user[0]["hash"], password):
            session["user_id"] = user["id"]
            return redirect("/")
        else:
            message3 = "Invalid username Or Password"
            return render_template("message.html", message = message3)



@app.route("/register", methods=['GET','POST'])
def register():
    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")
        confirmpassword = request.form.get("confirmpassword")

        if not username:
            message1 = "You should Give A Username"
            return render_template("message.html", message = message1)
        if not password:
            message2 = "You Should Give A Password"
            return render_template("message.html", message = message2)
        if not confirmpassword:
            message3 = "You Should Do The Confirmation"
            return render_template("message.html", message = message3)
        if password != confirmpassword:
            message4 = "It's Not The Same Password"
            return render_template("message.html", message = message4)
        hash = generate_password_hash(password)

        try:
            new_user = db.execute("INSERT INTO users(username, hash) VALUES(?, ?)", username, hash)

        except:
            message5 = "Username already exist"
            return render_template("message.html", message = message5)
        session["user_id"] = new_user
        return redirect("/")


