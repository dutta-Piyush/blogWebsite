from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length


class BlogForm(FlaskForm):
    """Form for creating a new blog post."""

    title = StringField(
        label="Title",
        validators=[
            DataRequired(message="Title is required."),
            Length(min=5, max=200, message="Title must be between 5 and 200 characters.")
        ],
        render_kw={"placeholder": "Enter the blog post title"}
    )

    content = TextAreaField(
        label="Content",
        validators=[
            DataRequired(message="Content is required."),
            Length(min=10, message="Content must be at least 10 characters.")
        ],
        render_kw={"placeholder": "Write your blog post content here...", "rows": 10}
    )

    writer = StringField(
        label="Writer",
        validators=[DataRequired(), Length(max=40)],
        render_kw={"placeholder": "Written By..."}
    )

    category = SelectField(
        "Category",
        choices=[
            ("data-science", "Data Science"),
            ("data-engineering", "Data Engineering"),
            ("machine-learning", "Machine Learning"),
            ("nlp", "NLP"),
            ("ai", "Artificial Intelligence")
        ],
        validators=[DataRequired()]
    )

    submit = SubmitField("Create Blog")
