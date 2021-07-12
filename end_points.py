from magnetdl import Magnetdl
from flask import Flask
from flask_restplus import Api, Resource
from kick import paging
from magnetdl import get
import json


app = Flask(__name__)
api = Api(app)


class KickAss(Resource):
	def __init__(self, keyword):
		self.json = []
			
	def get(self, keyword):
		title, magnet, size, seeds = paging(keyword)

		for i in range(len(title)):
			self.json.append({"title": title[i],"size": size[i],
			"seeds": seeds[i], "magenet": magnet[i]})
		
		return self.json


# @app.route("/mydata/<key>/")
def magnetdl(key):
	data = get(key)

	return json.dumps(data)

app.add_url_rule("/mydata/<string:key>/", "mydata", magnetdl) 

api.add_resource(KickAss, "/kickcine/<string:keyword>/")

if __name__ == "__main__":
	app.run(debug=True)
