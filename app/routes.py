

from app import app,db,bcrypt
from app.form import Register,Login,NewBlog
from app.models import User,Blog
from flask import render_template,url_for,flash,redirect,request,abort
from flask_login import login_user,current_user,logout_user,login_required






@app.route('/')
@app.route('/home')
def home():
    
    blog = Blog.query.all()
    
    return render_template('home.html',blog=blog)

@app.route('/register',methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
        
   
    
    form = Register()
    if form.validate_on_submit():
        encryptedpassword = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data,email=form.email.data,password=encryptedpassword)
        db.session.add(user)
        db.session.commit()
        
    
        flash(f'Account created for {form.username.data} succefully,You can login now','success')
        return redirect(url_for('home'))
            
    return render_template('register.html',form= form)


@app.route('/login',methods=['GET','POST'])
def login():
    
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember= form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
            
        
        else:
            flash('Login error!!. Enter correct email and password','danger')
            
            
    return render_template('login.html',form = form)


@app.route('/logout')
def logout():
    logout_user()
    
    return redirect(url_for('home'))

@app.route('/profile')
@login_required
def profile():
    
    return render_template('profile.html')





@app.route('/blog/new',methods=['GET','POST'])
@login_required
def newblog():
    form = NewBlog()
    if form.validate_on_submit():
        blog = Blog(title=form.title.data, content=form.content.data,author=current_user )
        db.session.add(blog)
        db.session.commit()
        flash(f'Hello {current_user.username} post has been added', 'success')
        return redirect(url_for('home'))
    
    
    return render_template('newblog.html',form =form, header = 'New Post')


@app.route('/blog/delete/<int:post_id>',methods=['POST', 'GET'])
@login_required
def delete_post(post_id):
    posts = Blog.query.get(post_id)
    if posts.author == current_user:
        db.session.delete(posts)
        db.session.commit()
        flash('Your pitch has been deleted','success')
    return redirect(url_for('home'))





    
    
    
    
    
    
    
    

  