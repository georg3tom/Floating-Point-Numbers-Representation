#!/bin/env python3
from flask import Flask, jsonify, render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
db.create_all()

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
    submit = request.args.get('subm')
    if int(submit) == 1 and request.args.get('q1') != None and request.args.get('q2') != None \
    and request.args.get('q3') != None and request.args.get('q4') != None:
        a1=a2=a3=a4=a5=0;
        if(int(request.args.get('q1'))==None):
            a1=1;
        elif(int(request.args.get('q2'))==1):
            a2=1;
        elif(int(request.args.get('q3'))==1):
            a3=1;
        elif(int(request.args.get('q4'))==1):
            a4=1;
        return str(a1)+str(a2)+str(a3)+str(a4);
    else:
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
