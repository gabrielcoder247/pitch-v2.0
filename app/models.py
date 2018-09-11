from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from .import db
from datetime import datetime
from .import login_manager



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_hash = db.Column(db.String(255))
    pitches = db.relationship('Pitch',backref = 'user',lazy="dynamic")
    comments = db.relationship('Comment',backref = 'user',lazy="dynamic")
    


    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')



    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return 'User {}'.format(self.username)


class Pitch(db.Model):
    '''
    Pitch class to define Pitch Objects
    '''
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String)
    body = db.Column(db.String)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comments = db.relationship('Comment',backref = 'pitch',lazy="dynamic")
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    Category_id = db.Column(db.Integer,db.ForeignKey("categories.id"))


    def save_pitch(self):
        '''
        Function that saves pitches
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls,id):
        '''
        Function that queries the databse and returns all the pitches
        '''
        pitches = Pitch.query.filter_by(Category_id = id).all()

        return pitches

    # @classmethod
    # def get_pitches_by_category(cls,cat_id):
    #     '''
    #     Function that queries the databse and returns pitches based on the
    #     category passed to it
    #     '''
    #     return Pitch.query.filter_by(category_id= cat_id)




class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer,primary_key = True)
    comment= db.Column(db.String)
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitch.id'))
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    
   


    def save_comment(self):
        '''
        Function that saves comments
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_comments(cls):
        Comment.all_comments.clear()

    @classmethod
    def get_comments(cls,id):
        comments = Comment.query.filter_by(pitch_id=id).all()

        return comments



class Category(db.Model):
    '''
    Function that defines different categories of pitches
    '''
    __tablename__ ='categories'


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    pitches= db.relationship('Pitch',backref = 'category',lazy="dynamic")
    

    @classmethod
    def get_categories(cls):
        '''
        This function fetches all the categories from the database
        '''
        categories = Category.query.all()
        return categories
