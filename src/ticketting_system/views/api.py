# __author__ = 'shanshul'

import json
from flask.ext.classy import FlaskView, route
from ticketting_system import models as km
from flask import Response, request
from bson import json_util
from . import api_blueprint as app

class Station(FlaskView):
	def index(self):
		return "Working!"

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