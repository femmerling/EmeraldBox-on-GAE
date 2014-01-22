from google.appengine.ext import ndb

class ValidatedIntegerProperty(ndb.IntegerProperty):
	def _to_base_type(self, value):
		try: 
			return int(value)
		except:
			raise TypeError("No integer value found")

class ValidatedFloatProperty(ndb.FloatProperty):
	def _to_base_type(self,value):
		try:
			return float(value)
		except:
			raise TypeError("No float value found")

