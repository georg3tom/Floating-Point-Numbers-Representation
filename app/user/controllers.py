from flask import Blueprint, request, session, jsonify,render_template
from app import db
from .models import User,quizcheck

mod_user = Blueprint('user', __name__, url_prefix='/')

@mod_user.route("/")
@mod_user.route("/introduction")
def intro():
    return render_template("introduction.html")

@mod_user.route("/theory")
def theory():
    return render_template("theory.html")

@mod_user.route("/objective")
def objective():
    return render_template("objective.html")

@mod_user.route("/experiment")
def exp():
    return render_template("experiment.html")

@mod_user.route("/manual")
def manual():
    return render_template("manual.html")

@mod_user.route("/quizzes")
def quizzes():
    if request.args.get('q1') != None and request.args.get('q2') != None \
    and request.args.get('q3') != None and request.args.get('q4') != None \
    and request.args.get('q5'):
        a1=a2=a3=a4=a5=0;
        a=[]
        a[0]=request.args.get('q1')
        a[1]=request.args.get('q2')
        a[2]=request.args.get('q3')
        a[3]=request.args.get('q4')
        a[4]=request.args.get('q5')
        return str(quizcheck(a))
        # if(int(request.args.get('q1'))==None):
        #     a1=1;
        # elif(int(request.args.get('q2'))==1):
        #     a2=1;
        # elif(int(request.args.get('q3'))==1):
        #     a3=1;
        # elif(int(request.args.get('q4'))==1):
        #     a4=1;
        # return str(a1)+str(a2)+str(a3)+str(a4);
    else:
        return render_template("quizzes.html")

@mod_user.route("/procedure")
def procedure():
    return render_template("procedure.html")

@mod_user.route("/refrences")
def references():
    return render_template("refrences.html")

@mod_user.route("/q/<q>")
def referes(q):
    user=User.query.all()
    bourne={}
    for usr in user:
        return str(usr.check(q))

@mod_user.route("/feedback")
def feedback():
    return render_template("feedback.html")
