from flask_wtf import FlaskForm , RecaptchaField
from wtforms.fields import StringField , PasswordField , SubmitField
from wtforms.validators import DataRequired , Length , Email , EqualTo

class login(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    email = StringField(name='email' , 
    validators=[DataRequired('Email Field Is Required') , Email('Email is InValid')])

    password = PasswordField(name='password' , 
    validators=[DataRequired('Password Field Is Required !') , 
    Length(min=8 , message='Password Is Less Than 8 Character')])

    submit = SubmitField()


class Register(FlaskForm):
    name = StringField(name='name' , 
    validators=[DataRequired('Name Field is Required')])

    email = StringField(name='email' , 
    validators=[DataRequired('Email Field Is Required') , Email('Email is InValid')])

    password = PasswordField(name='password' , 
    validators=[DataRequired('Password Field Is Required !') , 
    Length(min=8 , message='Password Is Less Than 8 Character')])

    confirm = PasswordField(name='confirm' , 
    validators=[DataRequired('Confirm Password Field Is Required !') , 
    Length(min=8 , message='Password Is Less Than 8 Character')
    ,EqualTo('password' , 'Confirm Does Not Match With Password')])

    recaptcha = RecaptchaField()

    submit = SubmitField('iufhcn')

class EditProfile(FlaskForm):
    name = StringField(name='name' , 
    validators=[DataRequired('Name Field is Required')])

    email = StringField(name='email' , 
    validators=[DataRequired('Email Field Is Required') , Email('Email is InValid')])

    phone = StringField(name='phone' , 
    validators=[DataRequired('Phone Field is Required')])

    submit = SubmitField('Update Profile')

class ChangePassword(FlaskForm):
    oldPassword = PasswordField(name='oldpassword' , 
    validators=[DataRequired('Old Password Field Is Required !') , 
    Length(min=8 , message='Password Is Less Than 8 Character')])

    newPassword = PasswordField(name='newpassword' , 
    validators=[DataRequired('New Password Field Is Required !') , 
    Length(min=8 , message='Password Is Less Than 8 Character')])

    confirm = PasswordField(name='confirm' , 
    validators=[DataRequired('Confirm Password Field Is Required !') , 
    Length(min=8 , message='Password Is Less Than 8 Character')
    ,EqualTo('newPassword' , 'Confirm Does Not Match With Password')])

    submit = SubmitField('Change Password')




