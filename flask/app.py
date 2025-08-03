import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
from random import randint
from flask_moment import Moment
from flask_login import LoginManager, login_required, current_user, logout_user
import re
from werkzeug.security import generate_password_hash, check_password_hash
from validators.Auth import login, Register, EditProfile, ChangePassword
from flask import render_template, request, redirect, url_for, flash

app = Flask(__name__)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'blog.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = '859259f695852ec0e666'

db = SQLAlchemy(app)

@app.route('/')
def home():
    return 'Hello, Flask is working!'

if __name__ == '__main__':
    app.run(port=8000, debug=True)