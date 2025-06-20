# from app import db, app
# from src.Blueprints.HomeBP import models

from src import db, create_app

# Import models so SQLAlchemy knows about them
from src.Blueprints.PostBP import models

app = create_app()

with app.app_context():
    db.create_all()