from utils_app.db import db
from datetime import datetime

class Todos(db.Model) # type: ignore
	"""
	Campos de tabla todos:
		id_todo : int 
		user : int
		name : str
		completed : bool
		deadline : datetime
		status : int
	"""
	id_todo = db.Column(db.Integer, primary_key=True, nullable=False)
	user = db.Column(db.Integer, db.ForeignKey('usuarios.id_user'), nullable=False)
	name = db.Column(db.String(30), nullable=False)
	completed  = db.Column(db.Boolean, nullable=False)
	deadline = db.Column(db.DateTime, nullable=True)
	status = db.Column(db.Integer, db.ForeignKey('status.id_status'))

	def __init__(self, user : str, name : str, completed : bool, deadline : datetime, status : int) -> None:
		self.user  = user
		self.name = name
		self.completed = completed
		self.deadline = deadline
		self.status = status