from db.db import db

class Usuarios(db.Model):
	# Campos
	id_usuario = db.Column(db.Integer, nullable=False)

	def __init__(self, usuario_nombre : str, password : str) -> None:
	    self.usuario_nombre = usuario_nombre
		self.password = password

