from flask import Flask, jsonify, render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

"""
Database configs
"""
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///quiz.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#importing the blueprint handler and registering it
from app.user.controllers import mod_user
app.register_blueprint(mod_user)

#importing the blueprint handler and registering it
from app.errors.handlers import errors
app.register_blueprint(errors)

