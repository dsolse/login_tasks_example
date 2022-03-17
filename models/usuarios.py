from utils_app.db import db

class Usuarios(db.Model): # type: ignore
	# Campos
	"""
	Campos de tabla usuarios:
		id_user : str
		nickname : str
		password : str
		rank : str
	"""
	id_user = db.Column(db.Integer, primary_key=True, nullable=False)
	nickname = db.Column(db.String(50), nullable=False)
	password = db.Column(db.String(100), nullable=False)
	rank = db.Column(db.Boolean, nullable=False)

	def __init__(self, usuario_nombre : str, nickname : str, password : str, rank : bool) -> None:
		self.usuario_nombre = usuario_nombre
		self.password = password
		self.rank = rank
		self.nickname = nickname

