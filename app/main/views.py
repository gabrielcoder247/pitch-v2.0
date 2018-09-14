from flask import render_template,url_for,redirect, request, session, flash
from flask_login import login_required,current_user
from . import main
from .. import db,photos
from ..models import User, Category,Pitch, Comment 
from .forms import CommentForm, PitchForm,UpdateProfile,VoteForm 


@main.route('/')
def index():
    '''
    View function that return the index page and it's data
    '''
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



@main.route('/category/<int:id>')
def category(id):
    '''
    view category function that returns the pitches of that category
    '''
    category = Category.query.get(id)
    # title = f'{category.name} pitches'
    pitch = Pitch.get_pitches_by_category(id)

    return render_template('category.html', category = category, pitch = pitch)

@main.route('/category/pitch/new/', methods = ["GET", "POST"])
@login_required
def new_pitch():
    '''
    view category that returns a form to create a pitch
    '''
    form = PitchForm()
    
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        # category = form.category.data

        # pitch instance
        new_pitch = Pitch(title = title, body = body, upvotes = 0, downvotes = 0,users = current_user)

         # save pitch
        new_pitch.save_pitch()  
        return redirect(url_for('.index'))
    return render_template('new_pitch.html', form = form)


@main.route('/category/pitch/comment/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):
    '''
    view category that returns a form to create a new comment
    '''
    form = CommentForm()
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

    

