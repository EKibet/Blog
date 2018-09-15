from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,PasswordField,SelectField, BooleanField, SubmitField
from wtforms.validators import ValidationError,  DataRequired,Length, Email, EqualTo
from app.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
    '''
    custom validators
    '''
    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Username is already taken.')
    
    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Email already exists')
    '''
    the two methods above issue database queries expecting there 
    will be no results. In the event a result already exists,
    a validation error is triggered by raising ValidationError
    '''
class PostForm(FlaskForm):
    title = TextAreaField(description='Blog Title', validators=[DataRequired()]) 
    post = TextAreaField(description='Blog Content', validators=[DataRequired()])
    category = SelectField('Category', choices=[('Education','Education'),('Technology','Technology'),('Business','Business'),('News','News'),('General','General')])
    submit = SubmitField(('Publish'))

class CommentForm(FlaskForm):
    details = StringField('Write a comment',validators=[DataRequired()])
    submit = SubmitField('Comment')