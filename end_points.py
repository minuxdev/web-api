from magnetdl import Magnetdl
from flask import Flask, render_template, redirect, url_for
from flask_restplus import Api, Resource
from kick import paging, root
#from magnetdl import get
import json
from time import strftime


app = Flask(__name__)
api = Api(app)

time = strftime("%Y-%M-%d %H:%M:%S")

class KickAss(Resource):
	def __init__(self, keyword):
		self.json = []
			
	def get(self, keyword):
		title, magnet, size, seeds = paging(keyword)

		for i in range(len(title)):
			self.json.append({"title": title[i],"size": size[i],
			"seeds": seeds[i], "magenet": magnet[i]})
		
		return self.json

def response(title, magnet, size, seeds):
	jsonfile = []

	for i in range(len(title)):
		jsonfile.append({
				"title": title[i],
				"size": size[i],
				"seeds": int(seeds[i]),
				"magnet": magnet[i]
		})

	return jsonfile


@app.route("/<keyword>/")
def search(keyword):
	title, magnet, size, seeds = paging(keyword)
	jsonfile = response(title, magnet, size, seeds)
	return render_template("db.html", data = jsonfile, time = time, 
		_title = "Results")



@app.route("/news")
def index():
	title, magnet, size, seeds = root()
	jsonfile = response(title, magnet, size, seeds)

	return render_template("db.html", data = jsonfile, time = time, _title = "News")
	

if __name__ == "__main__":
	# app.run()
	app.run(debug=True)
