from flask_sqlalchemy import SQLAlchemy
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ans = db.Column(db.Integer)
    def __init__(self, id,ans):
        self.id=id
        self.ans=ans

