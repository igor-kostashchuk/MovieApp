
def create_app():
    from flask import Flask
    import os
    app = Flask(__name__, static_url_path="/static", template_folder='../templates', static_folder='../static')
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")


    from .extensions import login_manager, db

    db.init_app(app)
    login_manager.init_app(app)
    with app.app_context():
        db.create_all()
    from app.vievs import core
    app.register_blueprint(core)
    from users.vievs import users
    app.register_blueprint(users)
    return app