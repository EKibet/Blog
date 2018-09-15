from flask import render_template,flash,abort,redirect,url_for,request

from flask_login import login_required,current_user

from . import main
from .forms import RegistrationForm,PostForm
from app.models import Post
from app import db
@main.route('/')
def index():
    registration_form = RegistrationForm()
    return render_template('index.html',registration_form=registration_form)

@main.route('/writer/dashboard', methods=['GET','POST'])
@login_required
def writer_dashboard():
    post_form = PostForm()
    if post_form.validate_on_submit():
        user = current_user
        new_post = Post(title = post_form.title.data,post_content=post_form.post.data,category = post_form.category.data,user = user)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('main.index',uname = user.username))
    posts = Post.query.all()
    return render_template('dashboard.html',PostForm=post_form,posts=posts)

@main.route('/comments/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):
    comment = Comments.query.filter_by(pitch_id=id).all()

    form_comment = CommentForm()
    if form_comment.validate_on_submit():
        details = form_comment.details.data

        new_comment = Comments(details = details,pitch_id=id,user=current_user)
        # # save comment
        db.session.add(new_comment)
        db.session.commit()

    return render_template('comments.html',form_comment = form_comment,comment=comment)