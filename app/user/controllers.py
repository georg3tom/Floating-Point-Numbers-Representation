from flask import Blueprint, request, session, jsonify,render_template
from app import db
from .models import Quiz,quizcheck
import random
from .exp import float_bin,decimal_converter,IEEE754

mod_user = Blueprint('user', __name__, url_prefix='/')

#Contains routes for all main pages
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

@mod_user.route("/experiment/<arg>")
def ieee(arg):
    try:
        ret=IEEE754(float(arg))
    except:
        #validation failed
        bourne={}
        bourne['status']="fail"
        return jsonify(bourne)
    return ret

@mod_user.route("/manual")
def manual():
    return render_template("manual.html")

@mod_user.route("/quizzes")
def quizzes():
    if request.args.get('q1') != None and request.args.get('q2') != None \
    and request.args.get('q3') != None and request.args.get('q4') != None:
        a1=a2=a3=a4=a5=0;
        a=[] #contains option marked by the user
        b=[] #contains the question ID
        a.append(request.args.get('q1'))
        b.append(request.args.get('q11'))
        a.append(request.args.get('q2'))
        b.append(request.args.get('q22'))
        a.append(request.args.get('q3'))
        b.append(request.args.get('q33'))
        a.append(request.args.get('q4'))
        b.append(request.args.get('q44'))
        #quiz check returns a string with zeros and ones (mentioned in quiz.js)
        return str(quizcheck(a,b))
    else:
        qess=random.sample(range(1,9),4)
        try:
            user=Quiz.query.all()
        except:
            return render_template('error/500.html')
        args=[]
        bourne={}
        i=1
        for usr in user:
            if usr.id in qess:
                bourne={}
                bourne['n']=i
                bourne['id']=usr.id
                bourne['ques']=usr.question
                bourne['ans']=usr.ans
                bourne['a1']=usr.a1
                bourne['a2']=usr.a2
                bourne['a3']=usr.a3
                bourne['a4']=usr.a4
                i+=1
                args.append(bourne)
        # return str(args)
        # args contains shiffled quiz # QUESTION&ANS
        return render_template("quizzes.html",args=args)

@mod_user.route("/procedure")
def procedure():
    return render_template("procedure.html")

@mod_user.route("/references")
def references():
    return render_template("references.html")

@mod_user.route("/q")
def referes():
    user=Quiz.query.all()
    bourne={}
    i=0
    for usr in user:
        bourne[str(i)+"ans"]=usr.ans
        bourne[str(i)+"qs"]=usr.question
        bourne[str(i)+"a1"]=usr.a1
        bourne[str(i)+"a2"]=usr.a2
        bourne[str(i)+"a3"]=usr.a3
        bourne[str(i)+"a4"]=usr.a4
        i=i+1
    return jsonify(bourne)

@mod_user.route("/feedback")
def feedback():
    return render_template("feedback.html")
