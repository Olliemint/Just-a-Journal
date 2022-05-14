from datetime import datetime
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
    image = db.Column(db.String(60), nullable=False, default ='default.jpg')
    posted = db.Column(db.DateTime,nullable = False, default = datetime.utcnow)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    
    
    
    def __repr__(self):
        
        return f"User('{self.title}','{self.category}','{self.content}','{self.posted}')"    