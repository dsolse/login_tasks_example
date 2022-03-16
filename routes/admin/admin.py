from flask import Blueprint
from flask.templating import render_template

admin_blueprint = Blueprint("admin", __name__, url_prefix="/admin")

@admin_blueprint.route('/')
def home():
    return render_template('admin/home.html')

@admin_blueprint.route("/register")
def register():
    return render_template("admin/register.html")

@admin_blueprint.route("/todos")
def todos():
    return render_template("admin/todos.html")