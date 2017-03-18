# Config File - to separate our app’s logic from static variables.

import os

# grab the folder where the script lives
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'siri_yangu'

# define full path for the DATABASE
DATABASE_PATH = os.path.join(basedir, DATABASE)
