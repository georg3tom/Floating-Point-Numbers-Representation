from flask_sqlalchemy import SQLAlchemy
# from app import db
from .models import Quiz

def dbfill():
    db.create_all()
    ar=['op1','op2','op3','op4']
    an=Quiz(1,2,"qs 1",ar)
    db.session.add(an)
    an=Quiz(2,1,'qs 2',ar)
    db.session.add(an)
    an=Quiz(3,4,'qs 3',ar)
    db.session.add(an)
    an=Quiz(4,2,'qs 4',ar)
    db.session.add(an)
    an=Quiz(5,4,'qs 5',ar)
    db.session.add(an)
    an=Quiz(6,3,'qs 6',ar)
    db.session.add(an)
    an=Quiz(7,1,'qs 7',ar)
    db.session.add(an)
    an=Quiz(8,2,'qs 8',ar)
    db.session.add(an)
