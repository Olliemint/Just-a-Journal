from datetime import datetime
from app import db,login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String,unique=True ,nullable=False)
    email = db.Column(db.String,unique=True,nullable=False)
    password = db.Column(db.String,nullable =False)
    posts = db.relationship("Blog", backref='author', lazy =True)
    
    
    def __repr__(self):
        
        return f"User('{self.username}','{self.email}')"
    
    
class Blog(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String,nullable=False)
    content = db.Column(db.String,nullable=False)
    image = db.Column(db.String(60), nullable=False)
    posted = db.Column(db.DateTime,nullable = False, default = datetime.utcnow)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    
    
    
    def __repr__(self):
        
        return f"User('{self.title}','{self.content}','{self.posted}')"    