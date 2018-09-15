from flask import render_template,flash,abort,redirect,url_for,request

from flask_login import login_required,current_user

from . import main
from .forms import RegistrationForm,PostForm,CommentForm
from app.models import Post,Comments
from app import db
@main.route('/')
def index():
    registration_form = RegistrationForm()
    return render_template('index.html',registration_form=registration_form)

@main.route('/writer/dashboard', methods=['GET','POST'])
@login_required
def writer_dashboard():
    post_form = PostForm()
    form_comment = CommentForm()
    if post_form.validate_on_submit():
        user = current_user
        new_post = Post(title = post_form.title.data,post_content=post_form.post.data,category = post_form.category.data,user = user)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('main.writer_dashboard',PostForm=post_form,form_comment=form_comment))
    posts = Post.query.all()
    return render_template('dashboard.html',PostForm=post_form,posts=posts,form_comment=form_comment)

@main.route('/comments/<int:id>', methods = ['GET','POST'])
@login_required
def new_comment(id):
    post_form = PostForm()

    form_comment = CommentForm()
    if form_comment.validate_on_submit():
        details = form_comment.details.data

        new_comment = Comments(details = details,post_id=id,user=current_user)
        # # save comment
        db.session.add(new_comment)
        db.session.commit()
    comment = Comments.query.filter_by(post_id=id).all()

    return render_template('dashboard.html',form_comment = form_comment,comment=comment,PostForm=post_form)


@main.route('/delete/<int:id>', methods=['POST','GET'])
def delete(id):

    try:
        post_form = PostForm()
        form_comment = CommentForm()
        posts = Post.query.all()

        fetched_comment = Post.query.filter_by(id=id).first()
        db.session.delete(fetched_comment)
        db.session.commit()
        posts = Post.query.all()

        return render_template('dashboard.html',form_comment = form_comment,posts=posts,PostForm=post_form)
    except Exception as e:
	    return(str(e))

        
# @app.route('/comments')
# def commentsdic():
# 	res = Comments.query.all()
# 	list_comments = [r.as_dict() for r in res]
# 	return jsonify(list_comments)


# @main.route('/comments/<int:id>', methods=['POST'])
# def process():

#     form_comment = CommentForm()
#     email = request.['email']
#     name = request.form_comment.['name']
    
#     if name and email:
# 		newName = name[::-1]

# 		return jsonify({'name' : newName})

# 	return jsonify({'error' : 'Missing data!'})