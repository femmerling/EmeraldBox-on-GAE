# do not change the following basic imports and configurations  if you still want to use box.py
import settings

from flask import Flask
app = Flask(__name__)
app.config.from_object('settings')

# flask imports
from flask import g
from flask import redirect
from flask import url_for
from flask import session
from flask import request
from flask import render_template
from flask import abort
from flask import flash
from flask import get_flashed_messages
from flask import json

# data model imports
from models import User, User, User

# you can freely change the lines below

# package imports
import logging
from datetime import datetime
from helpers import generate_key

# google api and library imports
from google.appengine.api import taskqueue, images, mail, urlfetch
from google.appengine.ext import ndb
from google.appengine.api.labs import taskqueue

# global variables

# home root controller
@app.route('/')
def index():
    #define your controller here
    return render_template('welcome.html')


########### user data model controllers area ###########

@app.route('/data/user/')
def data_user():
	# this is the controller for JSON data access
	user_list = User.query().fetch(10000)

	if user_list:
		json_result = json.dumps([user.dto() for user in user_list])
	else:
		json_result = None

	return json_result

@app.route('/user/')
def user_view_controller():
	#this is the controller to view all data in the model
	user_list = User.query().fetch(1000)

	if user_list:
		user_entries = [user.dto() for user in user_list]
	else:
		user_entries = None

	return render_template('user.html',user_entries = user_entries, title = "User List")

def get_single_user(user_id):
	user = None
	single_user = User.query(User_user_id == user_id).get()
	if single_user:
		user = single_user.dto()
	result = dict(user = user)
	return result

@app.route('/user/<user_id>.json')
def get_single_user_json(user_id):
	#this is the controller to get single entry in json format
	result = json.dumps(get_single_user(user_id))
	return result

@app.route('/user/<user_id>')
def view_single_user(user_id):
	#this is the controller to get single entry view
	user = get_single_user(user_id)
	return render_template(user_view.html, user = user)

@app.route('/user/add/')
def user_add_controller():
	#this is the controller to add new model entries
	return render_template('user_add.html', title = "Add New Entry")

@app.route('/user/create/',methods=['POST','GET'])
def user_create_data_controller():
	# this is the user data create handler
	username = request.values.get('username')
	firstname = request.values.get('firstname')
	lastname = request.values.get('lastname')
	user_new_id = generate_key()

	new_user = User(
									user_id = user_new_id,
									username = username,
									firstname = firstname,
									lastname = lastname
								)

	new_user.put()

	return 'data input successful <a href="/user/">back to Entries</a>'

@app.route('/user/edit/<id>')
def user_edit_controller(id):
	#this is the controller to edit model entries
	user_item = User.query(User.user_id == id).get()
	return render_template('user_edit.html', user_item = user_item, title = "Edit Entries")

@app.route('/user/update/<id>',methods=['POST','GET'])
def user_update_data_controller(id):
	# this is the user data update handler
	username = request.values.get('username')
	firstname = request.values.get('firstname')
	lastname = request.values.get('lastname')
	user_item = User.query(User.user_id == id).get()
	user_item.username = username
	user_item.firstname = firstname
	user_item.lastname = lastname

	User.put(user_item)

	return 'data update successful <a href="/user/">back to Entries</a>'

@app.route('/user/delete/<id>')
def user_delete_controller(id):
	#this is the controller to delete model entries
	user_item = User.query(User.user_id == id).get()

	user_item.key.delete()

	return 'data deletion successful <a href="/user/">back to Entries</a>'

