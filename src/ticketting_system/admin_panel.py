# __author__ = 'shanshul'


from . import admin
from models import *

from flask.ext.admin.contrib.mongoengine import ModelView

class TrainAdmin(ModelView):
    can_delete = False

admin.add_view(TrainAdmin(Train))

class UserAdmin(ModelView):
	can_delete = False

admin.add_view(UserAdmin(User))

class TicketAdmin(ModelView):
	can_delete = False

admin.add_view(TicketAdmin(Ticket))