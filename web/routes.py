# Web / 'routes.py'
from flask import Blueprint, render_template, request, redirect, url_for
from app import db 
from app.models import Services, Works, Client, Latest

web_bp = Blueprint('web', __name__, template_folder='templates', static_folder='static', static_url_path='web/static', url_prefix='/')

# Main Index Route
@web_bp.route('/')
def index():
    services = Services.query.all()
    works = Works.query.all()
    client = Client.query.all()
    latest = Latest.query.all()
    return render_template('web/index.html', services = services, works = works, client = client, latest = latest)

