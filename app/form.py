from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,BooleanField,TextAreaField,PasswordField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from app.models import User


class Register(FlaskForm):
    
    username = StringField('Username',validators=[DataRequired(),Length(min=4,max=15)])
    
    email = StringField('Email',validators=[DataRequired(),Email()])
    
    password = PasswordField('Password',validators=[DataRequired()])
    
    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    
    submit = SubmitField('Sign Up')
    
    
    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(f'{username.data} is already taken. Please choose another username')
        
    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(f'{email.data} is already taken. Please choose another email')     
    
    
class Login(FlaskForm):
    
    
    email = StringField('Email',validators=[DataRequired(),Email()])
    
    password = PasswordField('Password',validators=[DataRequired()])
    
    remember = BooleanField('Remember me')
    
    submit = SubmitField('Login') 
    
    
    
class NewBlog(FlaskForm):
    title = StringField('Post Title', validators=[DataRequired()])
    content = TextAreaField('Content',validators=[DataRequired()])
    submit = SubmitField('Post')    
    
    
class Subscribe(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    
    submit = SubmitField('Subscribe')  
    
    
    
class CommentForm(FlaskForm):
    comment = TextAreaField('Comment',validators=[DataRequired()])
    submit = SubmitField('Add')        
    