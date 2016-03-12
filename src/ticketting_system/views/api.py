# __author__ = 'shanshul'

import json
from flask.ext.classy import FlaskView, route
from ticketting_system import models as km
from flask import Response, request, render_template, send_from_directory
from bson import json_util
from . import api_blueprint as app
from decorators import pushlish_to_clickstream, write_to_elastic_search

class Station(FlaskView):
	@pushlish_to_clickstream
	def index(self):
		return "Working!"

	@pushlish_to_clickstream
	def get(self, s_id):
		try:
			station = km.Station.objects.get(id=s_id)
			return Response(json.dumps(station.to_json(), default=json_util.default), status=200, content_type="application/json")
		except Exception,e:
			return Response(json.dumps({'details':'Exception: %s'%repr(e)}), status=403, content_type="application/json")

	def post(self):
		data = request.form
		if not data:
			data = request.json

		keys = data.keys()
		station = km.Station()
		if 'name' in keys:
			station.name = data['name']
		if 'code' in keys:
			station.code = data['code']
		try:
			station.save()
			return Response(json.dumps(station.to_json(), default=json_util.default), status=200, content_type="application/json")
		except Exception,e:
			return Response(json.dumps({'details':'Exception: %s'%repr(e)}), status=403, content_type="application/json")


Station.register(app)

@app.route("/push_to_clickstream")
def push_to_clickstream():
	write_to_elastic_search()
	return "Success"

@app.route("/")
def return_furlencoHtml():
	write_to_elastic_search()
	return render_template("furlenco.html")

@app.route("/categories")
def return_cat():
	write_to_elastic_search()
	return render_template("categories.html")

@app.route("/packages")
def return_pack():
	write_to_elastic_search()
	return render_template("packages.html")


