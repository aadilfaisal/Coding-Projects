from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME= "database.db"
def create_app():
    
    app= Flask(__name__)
    app.config['SECRET_KEY']= 'DABDABADOO'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + DB_NAME
    ADMIN_PHONE_NUMBER = "0123456789"

    db.init_app(app)
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User,Orders,Product,Cart

    with app.app_context():
        db.create_all()

    create_database(app)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'  # Specify the login view for Flask-Login
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(phone):
        user = User.query.get(int(phone))
        print(f"Loaded user: {user}")
        return user

    return app
def create_database(app):
    db_path = path.join(app.root_path, DB_NAME)
    if not path.exists(db_path):
        db.create_all(app=app)
        print("Created Database!")
