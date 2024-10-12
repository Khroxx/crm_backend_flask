from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from .config import Config


db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from .models import AdminUser, Employee, Customer, Project, Group
    admin = Admin(app, name='Flask CRM Admin', template_mode='bootstrap3', url='/adminpanel')
    admin.add_view(ModelView(AdminUser, db.session))
    admin.add_view(ModelView(Employee, db.session))
    admin.add_view(ModelView(Customer, db.session))
    admin.add_view(ModelView(Project, db.session))
    admin.add_view(ModelView(Group, db.session))


    from .routes import main
    app.register_blueprint(main)

    return app
