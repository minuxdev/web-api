import json
from scrap_module import returning_json


def create_file(keyword, url):
	out_json = returning_json(url)
	if len(out_json) == 0:
		return out_json
	else:
		with open(f"./stored_files/{keyword}.json", "w") as js:
			js.write(json.dumps(out_json, indent = 4, ensure_ascii = False,
				separators=(',', ': ')))
		return out_json


def read_file(file):
	with open(file, "rb") as f:
		b_file = f.read()

	return b_file


def crate_db_ob(keyword):

	byte_file = read_file(f"./stored_files/{keyword}.json")

	statement = "INSERT INTO json (query, json_file) VALUES(%s,%s)"
	values = (f'{keyword}', byte_file)

	db_object = statement, values

	return db_object

