from flask_mail import Message
from flask import render_template
from . import mail
from threading import Thread
from app import create_app
from .decorators import async
@async
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def mail_message(subject,template,to,**kwargs):
    sender_email ='kibetedgar@gmail.com'

    email = Message(subject, sender=sender_email, recipients=[to])
    email.body= render_template(template + ".txt",**kwargs)
    email.html = render_template(template + ".html",**kwargs)
    mail.send(email)

def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()



