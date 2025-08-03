from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer , String , DateTime , Boolean , Column
from datetime import datetime
from werkzeug.security import generate_password_hash , check_password_hash
from flask_login import UserMixin

db = SQLAlchemy()

class Users(UserMixin,db.Model):
    """
    مدل کاربر برای سیستم احراز هویت و مدیریت کاربران
    """
    id = Column(Integer() , primary_key=True)
    name = Column(String(110))
    email = Column(String(110) , unique=True)
    password = Column(String(110))
    admin = Column(Boolean() , default=False)
    avatar = Column(String(110)  ,default='/static/img/avatar.jpg')
    phone = Column(String(20) , default = '0')
    token = Column(String(150) , default=' ')
    created_at = Column(DateTime() , default=datetime.utcnow())

    @property
    def passwd(self):
        """
        دسترسی مستقیم به پسورد مجاز نیست
        """
        raise AttributeError('Access Forbidden')
    
    @passwd.setter
    def passwd(self , password):
        """
        ست کردن پسورد با هش کردن
        """
        self.password = generate_password_hash(password)
    
    def IsOriginalPassword(self , user_password):
        """
        بررسی صحت پسورد وارد شده
        """
        return check_password_hash(getattr(self, 'password', ''), user_password)
    

