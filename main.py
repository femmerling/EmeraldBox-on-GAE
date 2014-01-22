# do not change the following basic imports and configurations  if you still want to use box.py
import settings

from flask import Flask
app = Flask(__name__)
app.config.from_object('settings')

from controllers import base_view

app.register_blueprint(base_view)