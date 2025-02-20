from flask import Blueprint, render_template
from flask_login import login_required, login_manager
from app.extensions import db
from .models import User
from data import *

users = Blueprint("users", __name__, static_url_path="/static, template_folder= '../templates', static_folder='../static'")

@login_required
@users.route("/movies/favorite/<movie_id>", methods=["GET", "POST"])
def toggle_favorite_movie(movie_id):
    from flask_login import current_user
    from .models import FavoriteMovies
    from app.extensions import db


    favorite_movies = FavoriteMovies.query.filter_by(movie_id=movie_id, user = current_user).first()
    if favorite_movies:
        db.session.delete(favorite_movies)
        db.session.commit()

        movies = current_user.favorite_movies
        print(movies)
        return "deleted"

    fav_movie = FavoriteMovies(movie_id=movie_id, user=current_user)
    print(fav_movie)
    db.session.add(fav_movie)
    db.session.commit()

    movies = current_user.favorite_movies
    print(movies)

    return "saved"


@users.route('/registration', methods=['GET', 'POST'])
def registration():
    from flask import request, flash, redirect
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '').strip()

        print(f"Received data: username={username}, email={email}, password={password}")

        error = False

        user_exists = User.query.filter_by(email=email).first()
        print(f"User exists: {user_exists}")
        if user_exists:
            flash('User already exists', 'error')
            error = True

        if len(password) < 8:
            print("Password too short")
            flash('Password must be at least 8 characters long', 'error')
            error = True

        if not error:
            print("No errors, creating user...")
            new_user = User(username=username, email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful!', 'success')
            return redirect('/')
    return render_template('registration.html')
@users.route('/login', methods=['GET', 'POST'])
def login():
    from flask import request, flash, redirect
    from flask_login import login_user
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '').strip()


        error = False

        user = User.query.filter_by(email=email).first()
        print(f"User exists: {user}")
        if not user:
            flash('User is not exists', 'error')
            error = True

        elif password != user.password:
            flash('invalid password', 'error')

        else:
            login_user(user)
            return redirect('/')

    return render_template('login.html')
@users.route("/logout")
@login_required
def logout():
    from flask_login import logout_user
    from flask import redirect
    logout_user()
    return redirect("/")
@users.route("/profile")
def profile():
    from app.vievs import current_user

    favorite_movies = [get_movie_details(movie.movie_id) for movie in current_user.favorite_movies]
    print(favorite_movies)
    return render_template('profile.html', favorite_movies = favorite_movies)
