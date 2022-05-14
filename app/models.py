from re import T
from app.models import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String,unique=True ,nullable=False)
    email = db.Column(db.String,unique=True,nullable=False)
    password = db.Column(db.String,nullable =False)
    posts = db.relationship("Blog", backref='user', lazy =True)
    
    
    def __repr__(self):
        
        return f"User('{self.username}','{self.email}')"
    
class Blog(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String,nullable=False)
    category = db.Column(db.String,nullable=False)
    content = db.Column(db.String,nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)    