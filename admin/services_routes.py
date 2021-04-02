# Admin / 'services.py'
from flask import Blueprint, render_template, request, redirect, url_for
from app import app,db
from app.models import Services
from admin.forms import ServicesForm

services_bp = Blueprint('services', __name__, template_folder='templates', static_folder='static', static_url_path='admin/static', url_prefix='/admin')

# Admin Route
@services_bp.route('/')
def admin():
    return render_template('admin/index.html')

# Services Add Route
@services_bp.route('/services', methods=['GET','POST'])
def services():
    services = Services.query.all()
    form = ServicesForm()
    if request.method == 'POST':
        services = Services(
            title = form.title.data,
            icon = form.icon.data
        )
        db.session.add(services)
        db.session.commit()
        return redirect('/admin/services')
    return render_template('admin/services.html', form = form, services = services)

# Services Watch Route
@services_bp.route('/services/watch/<id>')
def services_watch(id):
    watchServices = Services.query.get(id)
    return render_template('admin/services_watch.html', watchservices = watchServices)

# Services Delete Route
@services_bp.route('/services/delete/<id>')
def services_delete(id):
    deleteServices = Services.query.get(id)
    db.session.delete(deleteServices)
    db.session.commit()
    return redirect('/admin/services')
