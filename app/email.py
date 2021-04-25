from flask_mail import Message
from flask import render_template
from . import mail

sender_email = 'ekmuraya@gmail.com'
subject_pref = 'Pitch-Piper'


def mail_message(subject, template, to, **kwargs):

    email = Message(subject_pref+subject, sender=sender_email, recipients=[to])
    email.body = render_template(template + ".txt", **kwargs)
    email.html = render_template(template + ".html", **kwargs)
    mail.send(email)
