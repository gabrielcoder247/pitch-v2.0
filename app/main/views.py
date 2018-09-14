from flask import render_template,url_for,redirect, request, session, flash
from flask_login import login_required,current_user
from . import main
from .. import db,photos
<<<<<<< HEAD
from ..models import User, Category,Pitch, Comment 
from .forms import CommentForm, PitchForm,UpdateProfile,VoteForm 
=======
from ..models import Pitch,User,Category,Comment
from .forms import PitchForm, CommentForm
>>>>>>> 3e64a2d57cc9000291e11f7aa738690ca5fea512

@main.route('/')
def index():
    '''
    view root page function that returns index page
    '''
<<<<<<< HEAD
    pitches= Pitch.query.all()
    title = 'Gabs Pitch App'

    return render_template('index.html', title = title, pitches = pitches)



@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)
    return render_template('profile/profile.html',user = user)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

=======
    category = Category.get_categories()
>>>>>>> 3e64a2d57cc9000291e11f7aa738690ca5fea512

    title = 'Home'
    return render_template('index.html', title = title, category = category)

@main.route('/category/<int:id>')
def category(id):
    '''
    view category function that returns the pitches of that category
    '''
    category = Category.query.get(id)
<<<<<<< HEAD
    # title = f'{category.name} pitches'
    pitch = Pitch.get_pitches_by_category(id)
=======
    pitch = Pitch.get_pitches(id)
>>>>>>> 3e64a2d57cc9000291e11f7aa738690ca5fea512

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

<<<<<<< HEAD
@main.route('/category/pitch/comment/new/<int:id>', methods = ['GET','POST'])
=======
@main.route('/pitch/comment/new/<int:id>', methods = ['GET','POST'])
>>>>>>> 3e64a2d57cc9000291e11f7aa738690ca5fea512
@login_required
def new_comment(id):
    '''
    view category that returns a form to create a new comment
    '''
    form = CommentForm()
<<<<<<< HEAD
    pitch = Pitch.query.filter_by(id = id)
    if form.validate_on_submit():
        comment = form.comment.data
        # comment instance
        new_comment = Comment( comment_id =id,  comment = comment, users = current_user)

        # save review 
        new_comment.save_comment()
        return redirect(url_for('.index'))

    # title = f'{pitch.title} comment'
    return render_template('new_comment.html',comment = comment, form = form, pitch = pitch)

    






@main.route('/category/<int:pitch_id>/comment/')
@login_required
def comment():
    '''
    view category that returns all reviews for a pitch
    '''
    

    pitch = Pitch.query.filter_by()
    comment = Comment.query.filter_by()
    # title = f'{pitch.title} review'

    return render_template('comment.html', pitch = pitch,comment = comment)

    

=======
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
>>>>>>> 3e64a2d57cc9000291e11f7aa738690ca5fea512
