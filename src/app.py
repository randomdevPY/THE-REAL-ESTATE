from flask import Flask, render_template
from routes.private.backend import backend_private
from routes.public.frontend import frontend_public
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION_URI

app = Flask(__name__)

# settings
app.secret_key = 'mysecret'
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# no cache
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

SQLAlchemy(app) 

app.register_blueprint(backend_private, url_prefix='/private')
app.register_blueprint(frontend_public, url_prefix='/public')