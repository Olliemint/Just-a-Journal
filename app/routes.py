from app import app
from app.form import Register

from flask import render_template,url_for,flash,redirect
#from flask_login import login_user,current_user,logout_user,login_required



posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]



@app.route('/')
@app.route('/home')
def home():
    
    
    
    return render_template('home.html', posts=posts)

@app.route('/register',methods=['GET','POST'])
def register():
   
    
    form = Register()
    if form.validate_on_submit():
     
        flash(f'Account created for {form.username.data} succefully,You can login now','success')
        return redirect(url_for('home'))
    
    return render_template('register.html',form= form)