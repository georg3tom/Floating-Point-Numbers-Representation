from flask_sqlalchemy import SQLAlchemy
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ans = db.Column(db.Integer)
    def __init__(self, id,ans):
        self.id=id
        self.ans=ans
    def check(self,op):
        return int(self.ans==int(op))
def quizcheck(a):
    user=User.query.all()
    i=0
    r=""
    for usr in user:
        if a[i]==str(usr.ans):
            r+="1"
        else:
            r+="0"
        i=i+1
    return r
