
def create_app():
    from flask import Flask
    app = Flask(__name__, static_url_path="/static", template_folder= '../templates', static_folder='../static')
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movie.db"
    app.config["SECRET_KEY"] = "key-password"

    from .extensions import login_manager, db
    from users.models import User, FavoriteMovies, Comment

    db.init_app(app)
    login_manager.init_app(app)
    with app.app_context():
        db.create_all()
    from app.vievs import core
    app.register_blueprint(core)
    from users.vievs import users
    app.register_blueprint(users)
    return app