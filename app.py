from flask import Flask, render_template, request, redirect, url_for, session, logging
from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

import os
dbdir = "sqlite:///" + os.path.abspath(os.getcwd()) + "database.db"

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), unique = True, nullable = False)
    password = db.Column(db.String(80), nullable = False)





@app.route("/")
def Inicio():
    return render_template("home.html")

@app.route("/Acercade")
def Acerca():
    return render_template("Acerca.html")

@app.route("/Trilladoras")
def Trilladoras():
    return render_template("Trilladoras.html")

@app.route("/Foro")
def Foro():
    return render_template("Foro.html")


@app.route("/registro",  methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        hashed_pw = generate_password_hash(request.form["Contraseña"], method = "sha256")
        new_user = Users(username = resquest.form["Usuario"], password = hashed_pw)
        db.session.add(new_user)
        bd.session.commit()
        return "Su registro fue exitoso."
    return render_template("registro.html")



@app.route("/login")
def loginn():
    return render_template("login.html")

if  __name__ == "__main__":
    db.create_all()
    app.run(debug = True)