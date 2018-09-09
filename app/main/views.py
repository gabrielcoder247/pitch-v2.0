from flask import render_template
from flask_login import login_required
from . import main

@main.route('/')
def index():
    '''
    View function that return the index page and it's data
    '''
    title = 'Welcome to make your pitches here '

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