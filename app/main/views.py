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
