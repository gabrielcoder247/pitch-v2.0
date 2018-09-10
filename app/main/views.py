from flask import render_template,url_for,redirect
from flask_login import login_required,current_user
from . import main
from .. import db,photos
from ..models import Pitch,User,Category
from .forms import PitchForm, CommentForm



@main.route('/')
def index():
    '''
    View function that return the index page and it's data
    '''
    category = Category.query.all()
    title = 'Gabs Pitch App'

    return render_template('index.html', title = title)

# @main.route('/movie/review/new/<int:id>', methods = ['GET','POST'])
# @login_required
# def new_review(id):

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


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
    title = f'{category.name} pitches'
    pitch = Pitch.query_all(category.id)

    return render_template('category.html', title = title, category = category, pitch = pitch)

@main.route('/category/pitch/new/<int:id>', methods = ["GET", "POST"])
@login_required
def new_pitch(id):
    '''
    view category that returns a form to create a pitch
    '''
    form = PitchForm()
    
    if form.validate_on_submit():
        title = form.title.data
        body = form.body.data
        category = form.category.data

        # pitch instance
        new_pitch = Pitch(category = category.id, title = title, body = body, user = current_user)

         # save pitch
        new_pitch.save_pitch()  
        return redirect(url_for('.category', id = category.id))
    title = f'{category.name} pitches'
    return render_template('pitch.html', title = title, pitch_form = form, category = category)


@main.route('/pitch/comment/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):
    '''
    view category that returns a form to create a new review
    '''
    form = CommentForm()
    if form.validate_on_submit():
        comment = form.comment.data

        # comment instance
        new_comment = Comment (pitch_id = pitch.id, comment = comment, user = current_user)

        # save review 
        new_review.save_review()
        return redirect(url_for('.reviews', id = pitch.id ))

    title = f'{pitch.title} review'
    return render_template('new-review.html', title = title, review_form = form, pitch = pitch)

@main.route('/pitch/reviews/<int:id>')
def comment(id):
    '''
    view category that returns all reviews for a pitch
    '''
    pitch_id  = Pitch.query.filter_by(id =id).all()
    comment = Review.query.filter_by(id =id).all()
    title = f'{pitch.title} review'

    return render_template('review.html', title = title, pitch = pitch, review = review)


# @main.route('/inteview/pitches/')
# def Creative_Ideas():

#     pitches= Pitch.get_all_pitches()
#     title = 'Pitch Creative Ideas'
#     return render_template('creative_ideas.html', title = title, pitches= pitches )


@main.route('/interviews/pitches/')
def interviews():
    '''
    View root page function that returns the interviews pitch page and its data
    '''
    title = 'Interviews'
    interviews_pitch = Pitch.query.filter_by(category = 'interviews').all()
    return render_template('categories/interviews.html', title = title, interviews_pitch = interviews_pitch)

@main.route('/sales/pitches/')
def sales():
    '''
    View root page function that returns the sales page and its data
    '''
    title = 'Sales'
    sales_pitch = Pitch.query.filter_by(category = 'sales')
    return render_template('categories/sales.html', title = title, sales_pitch= sales_pitch).all()

@main.route('/investments/pitches/')
def investments():
    '''
    View root page function that returns the investment pitch page and its data
    '''
    title = 'Investments'
    investments_pitch = Pitch.query.filter_by(category = 'investments').all()
    return render_template('categories/investments.html', title = title, investments_pitch= investments_pitch )

@main.route('/customers/pitches/')
def customers():
    '''
    View root page function that returns the customer pitch page and its data
    '''
    title = 'Customers'
    customers_pitch = Pitch.query.filter_by(category = 'customers').all()
    return render_template('categories/customers.html', title = title, customers_pitch = customers_pitch)

@main.route('/employees/pitches/')
def employees():
    '''
    View root page function that returns the employees pitch page and its data
    '''
    title = 'Employees'
    employees_pitch = Pitch.query.filter_by(category = 'employees').all()
    return render_template('categories/employees.html', title = title,  employees_pitch=  employees_pitch )







  