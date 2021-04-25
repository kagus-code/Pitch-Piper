from flask import render_template, redirect, url_for,abort
from .forms import UpdateProfile
from .. import db
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


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)
        
