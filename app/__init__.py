
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


app = Flask(__name__)
mail = Mail(app) # instantiate the mail class







app.config['SECRET_KEY']='journal'
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///blog.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'danger'


from app import routes
