from flask import Flask
from routes.admin.admin import admin_blueprint
from routes.main.main import main_blueprint

app = Flask(__name__)

app.register_blueprint(admin_blueprint)
app.register_blueprint(main_blueprint)



