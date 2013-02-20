# coding: UTF-8
##############################################
# models.py - ndb model definition file		 #
# the datastore implemented is ndb			 #
# this is due to performance considerations  #
##############################################
from google.appengine.ext import ndb

class User(ndb.Model):
	user_id = ndb.StringProperty()
	username = ndb.StringProperty()
	firstname = ndb.StringProperty()
	lastname = ndb.StringProperty()

	# data transfer object to form JSON
	def dto(self):
		return dict(
				user_id = self.user_id,
				username = self.username,
				firstname = self.firstname,
				lastname = self.lastname)
