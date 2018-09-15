from flask import render_template, request, redirect, url_for, flash, abort
from . import main
from ..models import User, Pitch, Comment, UpVote, DownVote
from flask_login import login_required, current_user
from .. import db, photos
from .forms import PitchForm, CommentForm, UpdateProfile
import markdown2

@main.route('/')
def index():
    '''
    root page function that returns the index page and its data
    '''
    title = "Welcome | One Minute Pitch"

    return render_template("index.html", title=title)

@main.route('/user/<uname>&<id_user>')
@login_required
def profile(uname, id_user):
    user = User.query.filter_by(username = uname).first()

    title = f"{uname.capitalize()}'s Profile"

    get_pitches = Pitch.query.filter_by(user_id = id_user).all()
    get_comments = Comment.query.filter_by(user_id = id_user).all()
    get_upvotes = UpVote.query.filter_by(id_user = id_user).all()
    get_downvotes = DownVote.query.filter_by(id_user = id_user).all()

    if user is None:
        abort(404)
    
    return render_template('profile/profile.html', user = user, title=title, pitches_no = get_pitches, comments_no = get_comments, likes_no = get_upvotes, dislikes_no = get_downvotes)

@main.route('/home/like/<int:id>', methods = ['GET','POST'])
@login_required
def like(id):
    get_pitches = UpVote.get_votes(id)
    valid_string = f'{current_user.id}:{id}'

    for get_pitch in get_pitches:
        to_str = f'{get_pitch}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.pitch',id=id))
        else:
            continue

    like_pitch = UpVote(user = current_user, pitching_id=id)
    like_pitch.save_vote()

    return redirect(url_for('main.pitch',id=id))

@main.route('/home/dislike/<int:id>', methods = ['GET','POST'])
@login_required
def dislike(id):
    get_pitches = DownVote.get_downvotes(id)
    valid_string = f'{current_user.id}:{id}'

    for get_pitch in get_pitches:
        to_str = f'{get_pitch}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.pitch',id=id))
        else:
            continue

    dislike_pitch = DownVote(user = current_user, pitching_id=id)
    dislike_pitch.save_vote()

    return redirect(url_for('main.pitch',id=id))

@main.route('/home', methods = ['GET', 'POST'])
@login_required
def home():
    pitch_form = PitchForm()
    
    if pitch_form.validate_on_submit():
        pitch = pitch_form.pitch.data
        cat = pitch_form.my_category.data

        new_pitch = Pitch(pitch_content=pitch, pitch_category = cat, user = current_user)
        new_pitch.save_pitch()

        return redirect(url_for('main.home'))

    all_pitches = Pitch.get_all_pitches()

    title = 'Home | One Minute Pitch'    
    return render_template('home.html', title = title, pitch_form = pitch_form, pitches = all_pitches)

@main.route('/pitch/<int:id>',methods = ['GET','POST'])
@login_required
def pitch(id):
    
    my_pitch = Pitch.query.get(id)
    comment_form = CommentForm()

    if id is None:
        abort(404)

    if comment_form.validate_on_submit():
        comment_data = comment_form.comment.data
        new_comment = Comment(comment_content = comment_data, pitch_id = id, user = current_user)
        new_comment.save_comment()

        return redirect(url_for('main.pitch',id=id))

    all_comments = Comment.get_comments(id)
    # print(all_comments)
    # format_comments = markdown2.markdown(all_comments.comment_content,extras=["code-friendly", "fenced-code-blocks"])

    up_likes = UpVote.get_votes(id)
    down_likes = DownVote.get_downvotes(id)

    title = 'Comment | One Minute Pitch'
    return render_template('pitch.html',pitch = my_pitch, comment_form = comment_form, comments = all_comments, title = title, likes = up_likes, dislikes=down_likes)

@main.route('/category/<cat>')
def category(cat):
    my_category = Pitch.get_category(cat)

    title = f'{cat} category | One Minute Pitch'

    return render_template('category.html', title=title, category=my_category)

@main.route('/user/<uname>/update', methods=['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)
    
    update_form = UpdateProfile()

    if update_form.validate_on_submit():
        user.bio = update_form.bio.data
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname = user.username,id_user=user.id))
    title = 'Update Bio'
    return render_template('profile/update.html', form=update_form, title = title)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        # user_photo = PhotoProfile(pic_path = path,user = user)
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname,id_user=current_user.id))















# from flask import render_template,url_for,redirect, request, session, flash
# from flask_login import login_required,current_user
# from . import main
# from .. import db,photos
# from ..models import User,Pitch, Comment,Sale 
# from .forms import CommentForm, PitchForm,UpdateProfile,SaleForm 

# @main.route('/')
# def index():
#     '''
#     view root page function that returns index page
#     '''
#     pitches= Pitch.query.all()
#     title = 'Gabs Pitch App'

#     return render_template('index.html', title = title, pitches = pitches)



# @main.route('/user/<uname>')
# def profile(uname):
#     user = User.query.filter_by(username = uname).first()

#     if user is None:
#         abort(404)
#     return render_template('profile/profile.html',user = user)

# @main.route('/user/<uname>/update/pic',methods= ['POST'])
# @login_required
# def update_pic(uname):
#     user = User.query.filter_by(username = uname).first()
#     if 'photo' in request.files:
#         filename = photos.save(request.files['photo'])
#         path = f'photos/{filename}'
#         user.profile_pic_path = path
#         db.session.commit()
#     return redirect(url_for('main.profile',uname=uname))


#     title = 'Home'
#     return render_template('index.html', title = title, category = category)

# @main.route('/category/<int:id>')
# def category(id):
#     '''
#     view category function that returns the pitches of that category
#     '''
#     category = Category.query.get(id)
#     # title = f'{category.name} pitches'
#     pitch = Pitch.get_pitches_by_category(id)

#     return render_template('category.html', category = category, pitch = pitch)

# @main.route('/category/pitch/new/<int:id>', methods = ["GET", "POST"])
# @login_required
# def new_pitch(id):
#     '''
#     view category that returns a form to create a pitch
#     '''
#     form = PitchForm()
#     category = Category.query.filter_by(id = id).first()
#     if form.validate_on_submit():
#         title = form.title.data
#         post = form.post.data

#         # pitch instance
#         new_pitch = Pitch(category_id = id, title = title, post = post, user = current_user)

#         # save pitch
#         new_pitch.save_pitch()  
#         return redirect(url_for('main.category', id = category.id))
#     title = f'{category.name} pitches'
#     return render_template('new_pitch.html', title = title, pitch_form = form, category = category)

# @main.route('/category/pitch/comment/new/<int:id>', methods = ['GET','POST'])
# @login_required
# def new_comment(id):
#     '''
#     view category that returns a form to create a new comment
#     '''
#     form = CommentForm()
#     pitch = Pitch.query.filter_by(id = id)
#     if form.validate_on_submit():
#         comment = form.comment.data
#         # comment instance
#         new_comment = Comment( comment_id =id,  comment = comment, users = current_user)

#         # save review 
#         new_comment.save_comment()
#         return redirect(url_for('.index'))

#     # title = f'{pitch.title} comment'
#     return render_template('new_comment.html',comment = comment, form = form, pitch = pitch)

    






# @main.route('/category/<int:pitch_id>/comment/')
# @login_required
# def comment():
#     '''
#     view category that returns all reviews for a pitch
#     '''
    

#     pitch = Pitch.query.filter_by()
#     comment = Comment.query.filter_by()
#     # title = f'{pitch.title} review'

#     return render_template('comment.html', pitch = pitch,comment = comment)

    

