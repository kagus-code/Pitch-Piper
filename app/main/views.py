from flask import render_template, request,redirect, url_for,abort
from .forms import UpdateProfile,SubmitPitch
from .. import db,photos
from ..models import User,Pitch
from . import main
from flask_login import login_required,current_user


@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    all_pitches = Pitch.query.all()
    Investor= Pitch.query.filter_by(pitch_category='Investor').all()
    Competition=Pitch.query.filter_by(pitch_category = 'Competition').all()
    Product = Pitch.query.filter_by(pitch_category='Product').all()



    title = "Pitch-piper Home"
    return render_template('index.html', title=title,AllPitches=all_pitches,Investor=Investor,Competition=Competition,Product=Product)


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

@main.route('/submit_Pitch',methods = ['GET', 'POST'])
@login_required
def submit_pitch():
    form = SubmitPitch()
    if form.validate_on_submit():
        pitch_title = form.pitch_title.data
        pitch_category= form.pitch_category.data
        pitch_post=form.pitch_post.data
        new_pitch = Pitch(pitch_title=pitch_title,pitch_category=pitch_category,pitch_post=pitch_post,user = current_user)

        new_pitch.save_pitch()

        return redirect(url_for('main.index'))

    return render_template ('submit_pitch.html',pitch_form=form)    


        
        



        
