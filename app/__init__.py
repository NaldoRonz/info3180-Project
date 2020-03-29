#Ronaldo M. Reid 620109753
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

csrf = CSRFProtect()
app = Flask(__name__)

# For Flask Form
app.config["SECRET_KEY"] = "9_!Nald&$K8Y{i5*_H3r3}4618542184$@qlShu)_Un3<2gGu57"

# Runs on port 5432 only works with default server postgres
#app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:RSK4LFEg@localhost/postgres"
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://ndxofyornrbxaj:040f57d0a135abe01ccf2eb608682da4364309979a2a1896ccf0228a845c767a@ec2-52-87-58-157.compute-1.amazonaws.com:5432/dogsv2e87av5k'

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#For File Upload
UPLOAD_FOLDER = "./app/static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 10*1024*1024

app.config.from_object(__name__)

csrf.init_app(app)
my_db = SQLAlchemy(app) 
from app import views, models
