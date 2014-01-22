import uuid
import base64
import re

def generate_key():
	"""
	generates a uuid, encodes it with base32 and strips it's padding.
	this reduces the string size from 32 to 26 chars.
	"""
	return base64.b32encode(uuid.uuid4().bytes).strip('=').lower()

def thousand_separator(x=0, sep='.', dot=','):
	"""
	creates a string of number separated by selected delimiters
	"""
	num, _, frac = str(x).partition(dot)
	num = re.sub(r'(\d{3})(?=\d)', r'\1'+sep, num[::-1])[::-1]
	if frac:
		num += dot + frac
	return num

def new_parser(passed_object, request_data):
	"""
    Maps passed request object from client into expected object.
    Use this for creation of new object by passing an instantiated 
    empty object into the passed_object variable
	"""
	for item, value in request_data.values.iteritems():
		if hasattr(passed_object, item) and value is not None:
			setattr(passed_object, item, value)
	return passed_object

def edit_parser(passed_object, request_data):
	"""
	Maps value from passed json object for data edit purposes.
	You need to pass in object resulting from query into the
	passed_object variable
	"""
	for item in request_data.values:
		if item != "id" and hasattr(passed_object, item) and request_data.values.get(item) != None:
			setattr(passed_object, item, request_data.values.get(item))
	return passed_object