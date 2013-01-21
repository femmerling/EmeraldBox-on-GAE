import settings

from flask import Flask
app = Flask(__name__)
app.config.from_object('settings')

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

from models import User

from google.appengine.api.labs import taskqueue

@app.route('/')
def index():
    """
    renders the index page template
    """
    return render_template('welcome.html')