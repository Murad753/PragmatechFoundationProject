from flask import Blueprint, render_template, request, redirect, url_for
from app import app, db
from app.models import Latest
from admin.forms import LatestForm
from werkzeug.utils import secure_filename
import os

latest_bp = Blueprint('latest', __name__, template_folder='templates', static_folder='static', static_url_path='admin/static', url_prefix='/admin')

# Latest Add Route
@latest_bp.route('/latest', methods=['GET','POST'])
def latest():
    form = LatestForm()
    latest = Latest.query.all()
    if request.method == 'POST':
        file = form.l_img.data
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        latest = Latest(
            l_title = form.l_title.data,
            l_url = form.l_url.data,
            l_content = form.l_content.data,
            l_img = filename
        )
        db.session.add(latest)
        db.session.commit()
        return redirect('/admin/latest')
    return render_template('admin/latest.html', form = form, latest = latest)

# Latest Watch Route
@latest_bp.route('/latest/watch/<id>')
def latest_watch(id):
    watchLatest = Latest.query.get(id)
    return render_template('admin/latest_watch.html', watchLatest = watchLatest)

# Latest Delete Route
@latest_bp.route('/latest/delete/<id>')
def latest_delete(id):
    deleteLatest = Latest.query.get(id)
    db.session.delete(deleteLatest)
    db.session.commit()
    return redirect('/admin/latest')