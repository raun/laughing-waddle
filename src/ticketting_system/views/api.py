# __author__ = 'shanshul'

import json
from flask.ext.classy import FlaskView, route
from ticketting_system import models as km
from flask import Response, request
from bson import json_util

class Train(FlaskView):
	def get(self, t_id):
		try:
			train = km.Train.objects.get(id=t_id)
			return Response(json.dumps(train.to_json(), default=json_util.default), status=200, content_type="application/json")
		except Exception,e:
			return Response(json.dumps({'details':'Exception: %s'%repr(e)}), status=403, content_type="application/json")