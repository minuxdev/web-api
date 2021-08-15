from db_config import sql

db = sql()

class Json(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	query = db.Column(db.String(20), unique=True)
	json_file = db.Column(db.LargeBinary)

	def __repr__(cls):
		return {
			"id": cls.id, "query": cls.query, "json_file": cls.json_file
		}

