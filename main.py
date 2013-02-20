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
import models

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
