from flask import Blueprint, render_template, flash, request, redirect, url_for
from src.Blueprints.PostBP.models import Blog

home_bp = Blueprint('homeBP', __name__)
blogView_bp = Blueprint('blogViewBP', __name__)

@home_bp.route('/', methods=['GET', 'POST'])
@home_bp.route('/home', methods=['GET', 'POST'])
def home():
    posts = Blog.query.all()
    return render_template('index.html', posts=posts)


@blogView_bp.route('/blog', methods=['GET', 'POST'])
def blog():
    blog_id = request.args.get('blog_id')
    blog=Blog.query.filter_by(id=blog_id).first()
    if blog:
        # flash(f'Blog Title - {blog.title}', 'success')
        return render_template('blog.html', blog=blog)
