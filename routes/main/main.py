from flask import Blueprint
from flask.templating import render_template

main_blueprint = Blueprint("main", __name__)

@main_blueprint.route("/")
def home():
    return render_template("main/home.html")

@main_blueprint.route("/register")
def register():
    return render_template("main/register.html")

@main_blueprint.route("/todos")
def todos():
    return render_template("main/todos.html")