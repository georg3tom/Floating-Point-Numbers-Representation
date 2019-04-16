from flask_sqlalchemy import SQLAlchemy
from app import db
from app.user.models import User

def dbfill():
    db.create_all()
    ar=['q1 op1','q1 op2',' q1 op3','q1 op4']
    an=User(1,2,"qs 1",ar)
    db.session.add(an)
    ar=['q2 op1','q2 op2',' q2 op3','q2 op4']
    an=User(2,1,'qs 2',ar)
    db.session.add(an)
    ar=['q3 op1','q3 op2',' q3 op3','q3 op4']
    an=User(3,4,'qs 3',ar)
    db.session.add(an)
    ar=['q4 op1','q4 op2',' q4 op3','q4 op4']
    an=User(4,2,'qs 4',ar)
    db.session.add(an)
    ar=['q5 op1','q5 op2',' q5 op3','q5 op4']
    an=User(5,3,'qs 5',ar)
    db.session.add(an)
    ar=['q6 op1','q6 op2',' q6 op3','q6 op4']
    an=User(6,3,'qs 6',ar)
    db.session.add(an)
    ar=['q7 op1','q7 op2',' q7 op3','q7 op4']
    an=User(7,1,'qs 7',ar)
    db.session.add(an)
    ar=['q8 op1','q8 op2',' q8 op3','q8 op4']
    an=User(8,2,'qs 8',ar)
    db.session.add(an)
    db.session.commit()
dbfill()
