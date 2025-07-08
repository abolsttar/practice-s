from app import db
from sqlalchemy import Integer , String , DateTime , Boolean , Column
from datetime import datetime
from werkzeug.security import generate_password_hash , check_password_hash
from flask_login import UserMixin

class Users(UserMixin,db.Model):
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
        raise AttributeError('Access Forbidden')
    
    @passwd.setter
    def passwd(self , password):
        self.password = generate_password_hash(password)
    
    def IsOriginalPassword(self , user_password):
        return check_password_hash(self.password , user_password)
    

