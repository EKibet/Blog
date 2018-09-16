from flask import render_template,flash,abort,redirect,url_for,request

from flask_login import login_required,current_user

from . import main
from .forms import RegistrationForm,PostForm,CommentForm
from app.models import Post,Comments
from app import db
@main.route('/')
def index():
    # form_comment = CommentForm()

    form_comment = CommentForm()
    # user=current_user
    # if current_user.is_authenticated:
    
    #     new_comment = Comments(details = str(request.form['comment']),post_id=str(request.form['post']),user=current_user)
    #     # # save commen
    #     db.session.add(new_comment)
    #     db.session.commit()
    #     newcomments=[new_comment]
    # if post_form.validate_on_submit():
    #     user = current_user
    #     new_post = Post(title = post_form.title.data,post_content=post_form.post.data,category = post_form.category.data,user = user)
    #     db.session.add(new_post)
    #     db.session.commit()
    #     return redirect(url_for('main.writer_dashboard',PostForm=post_form))
    posts = Post.query.all()
    return render_template('index.html',type='post',posts=posts)

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
    return render_template('dashboard.html',PostForm=post_form,type='post',posts=posts,form_comment=form_comment)

@main.route('/comments/<int:postid>', methods = ['GET','POST'])
@login_required
def new_comment(postid):
    post_form = PostForm()

    form_comment = CommentForm()
    user=current_user
    if current_user.is_authenticated:
    
        new_comment = Comments(details = str(request.form['comment']),post_id=str(request.form['post']),user=current_user)
        # # save commen
        db.session.add(new_comment)
        db.session.commit()
        newcomments=[new_comment]
        return render_template('dashboard.html',form_comment = form_comment,type='comment',comments=newcomments,PostForm=post_form,user=user)
    return ''

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