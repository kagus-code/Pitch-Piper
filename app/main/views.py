from flask import render_template, redirect, url_for,abort
from ..models import User
from . import main
from flask_login import login_required


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = "Pitch-piper Home"
    return render_template('index.html', title=title)


@main.route('/user/<uname>')
def profile(uname):
    user=User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user )
        
