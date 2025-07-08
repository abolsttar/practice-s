from validators.Auth import login, Register, EditProfile, ChangePassword
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os
from random import randint
from flask_moment import Moment
from flask_login import LoginManager, login_manager, login_required, current_user, logout_user

app = Flask(__name__)

app.secret_key = '859259f695852ec0e666'

login_manager = LoginManager()
login_manager.init_app(app)

UPLOAD_DIR = os.path.curdir + '/static/uploads/'
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

def allow_extension(filename):
    ext = filename[-3:]
    extension = {'png','jpg'}
    if not ext in extension:
        return False
    return True

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'blog.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_DIR'] = UPLOAD_DIR

db = SQLAlchemy(app)

moment = Moment(app)

from models import user

@app.cli.command("create-db")
def create_db():
    db.create_all()
    print("Database created successfully!")


 
@app.route('/')
def main():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def signin():
    form = login()  
    userID = request.args.get('find')

    if request.method == 'POST':
        username = request.form.get('username') 
        password = request.form['password']

        if form.validate():
            print('validate form successfully', username, password)

        if username == 'admin' and password == '87654321':
            return redirect(url_for('main'))
        else:
            return 'username or password is incorrect.'

    return render_template('login.html', form=form, userid=userID)

@app.route('/post/', defaults={'post_id': 1})
@app.route('/post/<int:post_id>')
def showpost(post_id):
    return render_template('post.html', postid=post_id)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = Register()
    if request.method == 'POST' and form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data

        existing_user = user.Users.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already exists!', 'danger')
            return redirect(url_for('signup'))

        newuser = user.Users(name=name, email=email, passwd=password)
        db.session.add(newuser)
        db.session.commit()
        flash('User  registered successfully!', 'success')
        return redirect(url_for('signin'))

    return render_template('/auth/signup.html', form=form)
# @app.route('/signup', methods =['GET', 'POST'])
# def signup():
#     form = Register()
#     if request.method == 'POST':
#         id = randint(1, 100000)
#         name = request.form['name']
#         email = request.form['email']
#         password = request.form['password']
#         newuser = user.Users(id= id, name= name, email= email, passwd=password)
#         if newuser:
#             flash('name already exists!', 'danger')
#             return redirect(url_for('signup'))  
#         db.session.add(newuser)
#         result = db.session.commit() 
        
#         if result:
#             flash('user chk', 'succes')
#             return redirect(url_for('signup'))
#         else :
#             flash('eror%55', 'danger')
#             return redirect(url_for('signup'))
#     return render_template('/auth/signup.html', form = form)

@app.route('/account')
@login_required
def account():
    return render_template('/account/index.html')


@app.route('/account/edit')
@login_required
def account_edit():
    form = EditProfile()
    if form.validate_on_submit():
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        user = db.session.query(user.users).filter_by(email = current_user.email).one()

        user.name = name
        user.email = email
        user.phone = phone

        db.session.add(user)
        db .session.commit()
        return redirect(url_for('account_info'))
    return render_template('/account/edit.html', form = form)

@app.route('/account/info')
def account_info():
    return render_template('/account/info.html')

@app.route('/account/changepassword.html', methods=['get', 'post'])
def account_password():
    form = ChangePassword() 
    if request.method == 'post':
        if form.validate_on_submit():
            oldPassword = request.form.get('oldPassword')
            user = db.session.query(user.users).filter_by(email = current_user.email).one()
            if not user.IsOriginalPassword(oldPassword):
                flash('old psassword chek', 'danger')
                return redirect(url_for('account_password'))
            newPassword = request.form.get('newPassword')
            user.passwd = newPassword
            db.session.add(user)
            db.session.commit()
            flash('password change successfullu', 'success')
            return redirect(url_for('account_password'))
    return render_template('/account/changepassword.html', form = form)


@app.route('/account/avatar', methods=['get', 'post'])
def account_avatar():
    if request.method == 'post' and 'avatar' in request.files:
        avatar = request.files['avatar']
        filename = avatar.filename
        fileSecure = secure_filename(filename)
        if not allow_extension(filename):
            flash('extension is not allowed', 'danger')
            return redirect(url_for("account_avatar"))
        avatar.save(os.path.join(app.config["UPLOAD_DIR"], fileSecure))
        user = db.session.query(user.users).filter_by(email = current_user.email).one()
        user.avatar =f'uplodads/{filename}'
        db.session.add(user)
        db.session.commit()
        flash('uploude is successfuly', 'success')
        return redirect(url_for(account_avatar))
    return render_template('/account/avatar.html')

@app.route('/logout')
@login_required
def logout():

    logout_user()
    return redirect(url_for('main'))


@login_manager.user_loader
def load_user(user_id):
    return user.query.get(int(user_id))

@app.errorhandler(404)
def Notfound(error):

    return render_template('404.html', error=error)

app.jinja_env.line_statement_prefix = '#'

if __name__ == '__main__':
    app.run(port=8000, debug=True)