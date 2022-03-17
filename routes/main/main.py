from flask import Blueprint, redirect
from flask.helpers import url_for
from flask.templating import render_template
from formularios.register_user_form import RegisterForm
from utils_app.bcrypt_service import bcrypt
from models.usuarios import Usuarios
from utils_app.db import db

main_blueprint = Blueprint("main", __name__)

@main_blueprint.route("/")
def home():
    return render_template("main/home.html")

@main_blueprint.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        nickname = form.nickname.data
        password  = form.password.data
        nombre = form.name.data
        hashed_password = bcrypt.generate_password_hash(password)
        newUser = Usuarios(nickname, nombre,  str(hashed_password), False)
        db.session.add(newUser)
        db.session.commit()
        return redirect(url_for("main.home"))
    return render_template("main/register.html", form=form)

@main_blueprint.route("/login")
def login():
    return 

@main_blueprint.route("/todos")
def todos():
    return render_template("main/todos.html")