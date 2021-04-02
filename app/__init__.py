# App / '__init__.py'

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/data.db'
app.config['UPLOAD_PATH'] = 'admin/static/uploads'
db = SQLAlchemy(app)
migrate = Migrate(app,db)

from app.models import Services, Works, Client
from admin.services_routes import services_bp
from admin.works_routes import works_bp
from admin.client_routes import client_bp
from web.routes import web_bp
from admin.latest_routes import latest_bp

app.register_blueprint(services_bp)
app.register_blueprint(works_bp)
app.register_blueprint(web_bp)
app.register_blueprint(client_bp)
app.register_blueprint(latest_bp)