from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField

## login and registration


class add_user_Form(FlaskForm):
    username = TextField('Username', id='username_create')
    email = TextField('Email')
    password = PasswordField('Password', id='pwd_create')

class delete_user_Form(FlaskForm):
    username = TextField('Username', id='username_delete')

class setting_password_Form(FlaskForm):
    username = TextField('Username', id='username_setting')
    password = PasswordField('Password', id='pwd_setting')

class change_password_Form(FlaskForm):
    origin_password = PasswordField('Type Origin Password', id='origin_assword')
    new_password = PasswordField('Type New Password', id='new_assword')
    new_password2 = PasswordField('Type New Password Again', id='new_assword2')