from flask_sqlalchemy import SQLAlchemy
from app import db
from app.user.models import User

def dbfill():
    db.create_all()
    an=User(1,2)
    db.session.add(an)
    an=User(2,1)
    db.session.add(an)
    an=User(3,4)
    db.session.add(an)
    an=User(4,2)
    db.session.add(an)
    an=User(5,4)
    db.session.add(an)
    db.session.commit()

dbfill()
