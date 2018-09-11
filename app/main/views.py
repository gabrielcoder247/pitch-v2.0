from flask import render_template,url_for,redirect
from flask_login import login_required,current_user
from . import main
from .. import db,photos
from ..models import Pitch,User,Category,Comment
from .forms import PitchForm, CommentForm

@main.route('/')
def index():
    '''
    view root page function that returns index page
    '''
    category = Category.get_categories()

    title = 'Home'
    return render_template('index.html', title = title, category = category)

@main.route('/category/<int:id>')
def category(id):
    '''
    view category function that returns the pitches of that category
    '''
    category = Category.query.get(id)
    pitch = Pitch.get_pitches(id)

    return render_template('category.html', category = category, pitch = pitch)

@main.route('/category/pitch/new/<int:id>', methods = ["GET", "POST"])
@login_required
def new_pitch(id):
    '''
    view category that returns a form to create a pitch
    '''
    form = PitchForm()
    category = Category.query.filter_by(id = id).first()
    if form.validate_on_submit():
        title = form.title.data
        post = form.post.data

        # pitch instance
        new_pitch = Pitch(category_id = id, title = title, post = post, user = current_user)

        # save pitch
        new_pitch.save_pitch()  
        return redirect(url_for('main.category', id = category.id))
    title = f'{category.name} pitches'
    return render_template('new_pitch.html', title = title, pitch_form = form, category = category)

@main.route('/pitch/comment/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):
    '''
    view category that returns a form to create a new comment
    '''
    form = CommentForm()
    pitch = Pitch.query.filter_by(id = id).first()
    if form.validate_on_submit():
        comment = form.comment.data

        # review instance
        new_comment = Comment(pitch_id = pitch.id, post_comment = comment, user = current_user)

        # save review 
        new_comment.save_comment()
        return redirect(url_for('.comments', id = pitch.id ))

    title = f'{pitch.title} comment'
    return render_template('new_comment.html', title = title, comment_form = form, pitch = pitch)

@main.route('/pitch/comments/<int:id>')
def comments(id):
    '''
    view category that returns all comments for a pitch
    '''
    pitch = Pitch.query.get(id)
    comment = Comment.get_comments(pitch.id)
    title = f'{pitch.title} comment'

    return render_template('comments.html', title = title, pitch = pitch, comment = comment)
