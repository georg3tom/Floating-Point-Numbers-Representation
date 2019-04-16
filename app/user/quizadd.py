from flask_sqlalchemy import SQLAlchemy
# from app import db
from .models import User

def dbfill():
    db.create_all()
    ar=['op1','op2','op3','op4']
    an=User(1,2,"qs 1",ar)
    db.session.add(an)
    an=User(2,1,'qs 2',ar)
    db.session.add(an)
    an=User(3,4,'qs 3',ar)
    db.session.add(an)
    an=User(4,2,'qs 4',ar)
    db.session.add(an)
    an=User(5,4,'qs 5',ar)
    db.session.add(an)
    an=User(6,3,'qs 6',ar)
    db.session.add(an)
    an=User(7,1,'qs 7',ar)
    db.session.add(an)
    an=User(8,2,'qs 8',ar)
    db.session.add(an)
