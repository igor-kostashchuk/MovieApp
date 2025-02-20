from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_login import LoginManager

class Base(DeclarativeBase):
    pass
db = SQLAlchemy(model_class=Base)
login_manager = LoginManager()
login_manager.login_view = "users.login"
@login_manager.user_loader
def load_user(user_id):
    from users.models import User
    return User.query.get(str(user_id))