from flask_sqlalchemy import SQLAlchemy
from app import db
from sqlalchemy.dialects.postgresql import ARRAY

class Quiz(db.Model):
    """
    Data model for database to store quiz Qs,Ans,Ops
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ans = db.Column(db.Integer)
    question=db.Column(db.String(220), unique=True, nullable=False)
    a1=db.Column(db.String(220), nullable=False)
    a2=db.Column(db.String(220), nullable=False)
    a3=db.Column(db.String(220), nullable=False)
    a4=db.Column(db.String(220), nullable=False)
    def __init__(self,id,cans,ques,ans):
        self.id=id
        self.ans=cans
        self.question=ques
        self.a1=ans[0]
        self.a2=ans[1]
        self.a3=ans[2]
        self.a4=ans[3]

    def check(self,op):
        return int(self.ans==int(op))

def quizcheck(a,b):
    """
    Function to evaluate users input
    """
    user=Quiz.query.all()
    j=0
    r=""
    for i in b:
        for usr in user:
            if  str(i) == str(usr.id):
                if str(a[j]) == str(usr.ans):
                    r+="1"
                    continue
                else:
                    r+="0"
                    continue
        j=j+1
    return r
