import os
DEBUG = os.environ.get('SERVER_SOFTWARE', 'Dev').startswith('Dev')
SECRET_KEY = 'j;wD=R#2]07l65r+J)9,%)D[f:1,VS.+RQ+5VY.]lP]\wY:K'
BASEDIR = os.path.abspath(os.path.dirname(__file__))
WHITE_SPACE = "\t"
VALID_DATA_TYPES = [
    'int','integer','float','bool','boolean','string','str','text','blob',
    'datetime','date','time','key','blobkey','geo','geopt','user',
    'structured','local','localstructured','json','pickle','generic','computed'
]

# CSRF_ENABLED=True
# CSRF_SESSION_LKEY=''
