#!/bin/env python3
from flask import Flask, jsonify, render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
db.create_all()
from app.user.controllers import mod_user
app.register_blueprint(mod_user)

