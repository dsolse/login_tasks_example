from db.db import db

class Usuarios(db.Model): # type: ignore
	# Campos
	"""
	Campos de tabla usuarios:
		id_user : str
		nickname : str
		password : str
	"""
	id_user = db.Column(db.Integer, primary_key=True, nullable=False)
	nickname = db.Column(db.String(50), nullable=False)
	password = db.Column(db.String(100), nullable=False)

	def __init__(self, usuario_nombre : str, nickname : str, password : str) -> None:
		self.usuario_nombre = usuario_nombre
		self.password = password
		self.nickname = nickname

