from . import db, login_manager
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash


class User(UserMixin, db.Model):
    '''
    UserMixin class that includes generic implementations
    that are appropriate for most user model classes
    '''
    __tablename__ = 'users'
    id =db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), index=True, unique = True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(130))
    bio = db.Column(db.String(255))
    profile_pic = db.Column(db.String(255))
    pitches = db.relationship('Post',backref = 'user',lazy = "dynamic")
    comments = db.relationship('Comments', backref='user', lazy="dynamic")


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)
        '''
    with these two methods in place, a user object is now 
    able to do secure password verification
    '''
    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)
    '''
    The new avatar() method of the User class returns the URL of the user's avatar image, 
    scaled to the requested size in pixels.For users that don't have an avatar registered, an "identicon" image will be generated
    The verify_reset_password_token() is a static method, which means that it can be invoked directly from the class
    '''
    def __repr__(self):
        return '{}'.format(self.username)
    '''
    Flask-login keeps track of the logged in 
    user by storing its unique identifier in Flask's
    user session.
    ''' 
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

class Post(db.Model):
    __tablename__= 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    post_content = db.Column(db.String(255))
    category = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime,index=True,default=datetime.utcnow)
    user_id = db.Column(db.Integer, 
                                    db.ForeignKey('users.id'))
    comments = db.relationship('Comments', 
                                    backref='coment', 
                                    lazy="dynamic")
    messages_sent = db.relationship('Message',
                                    foreign_keys='Message.sender_id',
                                    backref='author', lazy='dynamic')
    messages_received = db.relationship('Message',
                                        foreign_keys='Message.recipient_id',
                                        backref='recipient', lazy='dynamic')
    last_message_read_time = db.Column(db.DateTime)

    # ...

    def new_messages(self):
        last_read_time = self.last_message_read_time or datetime(1900, 1, 1)
        return Message.query.filter_by(recipient=self).filter(
            Message.timestamp > last_read_time).count()

            
    @classmethod
    def retrieve_posts(cls,id):
        posts = Post.filter_by(id=id).all()
        return posts
    '''
    Pitch class represent the pitches Pitched by 
    users. Timestamp is set to default and passsed datetime.utcnow--> function.
    SQLAlchemy will set the field to the value of calling that function
    and not the result of calling it without ()
    The user_id field is initialized as a foreign key to user.id,
    which means that it references an id value from the users table
    '''

    def __repr__(self):
        return '{}'.format(self.body)
       
class Comments(db.Model):
    __tablename__='comments'
    id = db.Column(db.Integer,primary_key= True)
    details = db.Column(db.String(255))
    post_id = db.Column(db.Integer,db.ForeignKey('posts.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

	# def as_dict(self):
    # 		return {'details': self.details}    

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return '<Message {}>'.format(self.body)