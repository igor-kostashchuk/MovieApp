from flask import Blueprint, render_template, request, flash
from flask_login import current_user, login_required
from data import *


core = Blueprint("core", __name__, static_url_path="/static", template_folder='../templates', static_folder='../static')

@core.route('/')
@core.route('/home')
def home():

    if current_user.is_authenticated:
        favorite_movies = [movie.movie_id for movie in current_user.favorite_movies]
        print(favorite_movies)
    else:
        favorite_movies = []

    movies = get_popular_movies()
    upcoming_movies = get_upcoming_movies()
    toprated_movies = get_toprated_movies()
    print(movies)
    return render_template("index.html",
                           movies=movies,
                           upcoming_movies=upcoming_movies,
                           toprated_movies=toprated_movies,
                           favorite_movies=favorite_movies)

@core.route('/movies/popular')
def popular_movies():
    from flask import request
    page = int(request.args.get('page', 1))
    movies = get_popular_movies(page)
    page_start_index = max(page-4, 1)
    page_end_index=page_start_index+10
    return render_template('movie_list.html',movies=movies, page_start_index=page_start_index,page_end_index=page_end_index )
@core.route('/movies/upcoming')
def upcoming_movies():
    from flask import request
    page=int(request.args.get('page', 1))
    movies=get_upcoming_movies(page)
    page_start_index=max(page-4, 1)
    page_end_index=page_start_index+10
    return render_template('movie_list.html',movies=movies, page_start_index=page_start_index,page_end_index=page_end_index )
@core.route('/movies/toprated')
def top_rated_movies():
    from flask import request
    page = int(request.args.get('page', 1))
    movies = get_toprated_movies(page)
    page_start_index = max(page-4, 1)
    page_end_index = page_start_index+10
    return render_template('movie_list.html',movies=movies, page_start_index=page_start_index,page_end_index=page_end_index )
@core.route('/movies/<movie_id>', methods=["GET", "POST"])
def movie_details(movie_id):
    from users.models import Comment
    from .extensions import db
    movie = get_movie_details(movie_id)
    images = get_movie_images(movie_id)
    similar = get_similar_movies(movie_id)

    fetched_videos = get_movie_video(movie_id)
    videos = [
        item
        for item in fetched_videos
        if item.get("type") == "Trailer" and item.get("official")
    ]
    print(videos[0])

    if len(videos) > 1:
        video_key = videos[0]["key"]
    elif len(fetched_videos) > 1:
        video_key = fetched_videos[0]["key"]
    else:
        video_key = None

    if request.method == "POST":
        content = request.form.get("content")
        if not content:
            flash("comment can not be empty", "error")
        else:
            comment = Comment(movie_id=movie_id, content=content, user=current_user)
            db.session.add(comment)
            db.session.commit()

    comments =Comment.query.filter_by(movie_id=movie_id).all()
    print(comments)
    return render_template('details.html', movie=movie, images=images, similar=similar, video_key=video_key, comments = comments)



@core.route('/delete_comment/<int:comment_id>', methods=['POST'])
@login_required
def delete_comment(comment_id):
    from users.models import Comment
    from .extensions import db
    from flask import Flask, request, jsonify
    comment = Comment.query.get_or_404(comment_id)

    if current_user.id == comment.user_id or current_user.is_admin:
        db.session.delete(comment)
        db.session.commit()
        return jsonify({"status": "success"}), 200
    else:
        return jsonify({"status:""error" "У вас немає прав для видалення цього коментаря"}), 403

@core.route("/movies/search")
def search():
    query = request.args.get("query", "")
    page = int(request.args.get('page', 1))
    movies = search_movies(query, page)

    page = int(request.args.get('page', 1))
    page_start_index = max(page - 4, 1)
    page_end_index = page_start_index + 10

    return render_template("movie_list.html", movies=movies, page_start_index=page_start_index,page_end_index=page_end_index,)