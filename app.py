from flask import Flask
from routes.admin.admin import admin_blueprint
from routes.main.main import main_blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)

app.register_blueprint(admin_blueprint)
app.register_blueprint(main_blueprint)
app.config.from_object('config.BaseConfig')

SQLAlchemy(app)
Bcrypt(app)


