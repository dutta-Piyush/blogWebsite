from datetime import datetime
from src import db

class Blog(db.Model):
    __tablename__ = "blogs"

    id = db.Column(db.String(50), primary_key=True, nullable=False)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(15), default="default", nullable=False)
    writer = db.Column(db.String(40), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.now)
