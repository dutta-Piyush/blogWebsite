#init.py

import os
from flask import Flask
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KEY", "fallback_key")
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
    db.init_app(app)

    # Import blueprints and models here to avoid circular imports
    from src.Blueprints.HomeBP.routes import home_bp, blogView_bp
    from src.Blueprints.PostBP.routes import blog_bp
    from src.Blueprints.PostBP import models

    app.register_blueprint(home_bp)
    app.register_blueprint(blog_bp)
    app.register_blueprint(blogView_bp)

    return app
