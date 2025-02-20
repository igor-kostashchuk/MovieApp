from datetime import datetime
from app.extensions import db
from flask_login import UserMixin
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    favorite_movies = db.relationship("FavoriteMovies", backref="user")
    comment = db.relationship("Comment", backref="user")


class FavoriteMovies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

class Comment(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    movie_id=db.Column(db.Integer, nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'))
    content=db.Column(db.Text,nullable=False)
    created_at=db.Column(db.DateTime,default=datetime.utcnow)
