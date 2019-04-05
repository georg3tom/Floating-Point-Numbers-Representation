#!/bin/env python3
from flask import Flask, jsonify, render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
@app.route("/introduction")
def intro():
    return render_template("introduction.html")

@app.route("/theory")
def theory():
    return render_template("theory.html")

@app.route("/objective")
def objective():
    return render_template("objective.html")

if __name__ == "__main__":
    app.run(debug=True)
