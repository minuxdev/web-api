from flask import Flask, render_template, redirect, url_for
from flask_restplus import Api, Resource
from scrap_module import data_collector, returning_json
import db_object_maker as dm
import json
from time import strftime
from db_config import sql
import pymysql
import psycopg2


pymysql.install_as_MySQLdb()

time = strftime("%Y-%M-%d %H:%M:%S")

app = Flask(__name__)
api = Api(app)

# mydb = 'mysql://minux: @localhost/json'
mydb = "postgresql://qzedlvfjvoimbs:488b23ab02f988a6bea5e86468bcaaef310d2496\
23ca100f917f3ad46752c68c@ec2-52-72-125-94.compute-1.amazonaws.com:\
5432/d3ep75ssohpk8d"
db = sql(app, mydb)


class Json(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	query = db.Column(db.String(20), unique=True)
	json_file = db.Column(db.LargeBinary)

	def __repr__(cls):
		return {
			"id": cls.id, "query": cls.query, "json_file": cls.json_file
		}


@app.route("/<keyword>/")
def search(keyword):

	url = f"https://kat.sx/usearch/{keyword}"
	out_json = dm.create_file(keyword, url)

	# Validating results
	if len(out_json) != 0:
		print("file found")
		print(len(out_json))
		binary_file = dm.read_file(f"./stored_files/{keyword}.json")


		# Inserting results into database
		try:
			db_object = Json(id = 2, query=keyword, json_file = binary_file)
			db.session.add(db_object)
			db.session.commit()
			print("Commited successfully")

		except OSError as e:
			print(f"Error: {e}")
		
		return render_template("db.html", data = out_json, time = time, 
			_title = "Results", page = keyword)

	else:
		print("Nothing found")
		return render_template("not_found.html")


@app.route("/db/")
def dbase():

	ob = db.session.query(Json).all()
	print(type(ob))
	return f"<p>{ob}</p>"


@app.route("/show/")
def index():
	url = f"https://kat.sx/tv"
	jsonfile = returning_json(url)

	return render_template("db.html", data = jsonfile, 
			time = time, _title = "TV Show", page = "TV Show")

@app.route("/movies/")	
def movies():
	url = f"https://kat.sx/movies"
	jsonfile = returning_json(url)

	return render_template("db.html", data = jsonfile, 
			time = time, _title = "Movies", page = "Movies")

if __name__ == "__main__":
	# app.run()
	app.run(debug=True)
