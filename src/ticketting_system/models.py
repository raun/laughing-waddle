# __author__ = 'shanshul'


from . import db
from datetime import datetime
from exceptions import ValidationException

class Station(db.Document):
	id = db.StringField(required=True)
	name = db.StringField(required=True)
	code = db.StringField(required=True)

	def __repr__(self):
		return self.id

	def __str__(self):
		return str(self.id + " : " + self.code)

class Couch(db.Document):
	id = db.StringField(required=True)
	seats_available = db.ListField(db.BooleanField())

	def save(self, *args, **kwargs):
		self.reset_seat_allocation()
		if len(self.seats_available) > 100:
			raise ValidationException
		super(Couch, self).save(*args, **kwargs)

	def reset_seat_allocation(self):
		self.seats_available = []
		for i in range(100):
			self.seats_available[i] = True

class Train(db.Document):
	id = db.StringField(required=True)
	name = db.StringField(required=True)
	is_active = db.BooleanField(default=True)
	is_deleted = db.BooleanField(default=False)
	added_on = db.DateTimeField()
	modified_on = db.DateTimeField()
	source = db.ReferenceField(Station)
	station_via = db.ListField(db.ReferenceField(Station))
	destination = db.ReferenceField(Station)
	departure_time = db.DateTimeField()
	arrival_time = db.DateTimeField()
	couches = db.ListField(db.ReferenceField(Couch))

	def save(self, *args, **kwargs):
		self.modified_on = datetime.now()
		if self.source == self.destination :
			raise ValidationException("Source & Destination can not be same")
		super(Train, self).save(*args, **kwargs)

	def __repr__(self):
		return self.id

	def __str__(self):
		return str(self.id + " : " + self.name)

	def reset_seat_allocation(self):
		for couch in self.couches:
			couch.reset_seat_allocation()

	def to_json(self):
		return {
			"id" : self.id,
			"name" : self.name,
			"is_active" : self.is_active,
			"is_deleted" : self.is_deleted,
			"source" : self.source.code,
			"destination" : self.destination.code
		}

class User(db.Document):
	id = db.StringField(required=True)
	name = db.StringField(required=True)
	age = db.StringField(required=True)

	def __str__(self):
		return str(self.id + " : " + self.name)

class Ticket(db.Document):
	id = db.StringField(required=True)
	user = db.ReferenceField(User)
	train = db.ReferenceField(Train)
	couch = db.ReferenceField(Couch)
	seat_no = db.IntField()
