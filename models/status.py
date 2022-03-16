from db.db import db

class Status(db.Model): # type: ignore
	"""
	Campos de status:
		id_status : int
		name : str
		desc : str
	"""
	id_status = db.Column(db.Integer, primary_key=True, nullable=False)
	name = db.Column(db.String(10), nullable = False)
	desc = db.Column(db.String(30), nullable=False)

	def __init__(self, name : str, desc : str) -> None:
		self.name = name
		self.desc = desc
