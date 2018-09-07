from flask import render_template
from . import main

@main.route('/')
def index():
    '''
    View function that return the index page and it's data
    '''
    title = 'Welcome to make your pitches here '

    return render_template('index.html', title = title)
