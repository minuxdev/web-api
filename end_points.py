from flask import Flask
from flask_restplus import Api, Resource

app = Flask(__name__)
api = Api(app)


class KickApi(Resource):
	def __init__(self, keyword)
	pass


api.url_roule("cinema", "cinema", "/cinema/<string:keyword>/")

if __name__ == "__main__":
	app.run()