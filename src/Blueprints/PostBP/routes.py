import uuid
from src import db
from flask import Blueprint, flash, redirect, url_for, render_template

from src.Blueprints.PostBP.forms import BlogForm
from src.Blueprints.PostBP.models import Blog


blog_bp = Blueprint('blogBP', __name__)


@blog_bp.route('/create', methods=['GET', 'POST'])
def create_blog():
    form = BlogForm()
    try:
        if form.validate_on_submit():
            blog = Blog(id=str(uuid.uuid4()), title=form.title.data, content=form.content.data, writer=form.writer.data)
            db.session.add(blog)
            try:
                db.session.commit()
            except Exception as e:
                print("Error committing to DB:", e)
                db.session.rollback()
                flash("Database error: " + str(e), "danger")
            flash("The Post creation is been successful", "success")
            return redirect(url_for("homeBP.home"))
    except Exception as e:
        print(f'The error is {e}')

    return render_template("create_blog.html", form=form)
