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

@app.route("/experiment")
def exp():
    return render_template("experiment.html")

@app.route("/manual")
def manual():
    return render_template("manual.html")

@app.route("/quizzes")
def quizzes():
    return render_template("quizzes.html")

@app.route("/procedure")
def procedure():
    return render_template("procedure.html")

@app.route("/refrences")
def references():
    return render_template("refrences.html")

@app.route("/feedback")
def feedback():
    return render_template("feedback.html")

if __name__ == "__main__":
    app.run(debug=True)
