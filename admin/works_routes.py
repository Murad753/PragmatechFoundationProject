# Admin / 'works.py'
from flask import Blueprint, render_template, request, redirect, url_for
from app import app,db
from app.models import Works
from admin.forms import WorksForm
from werkzeug.utils import secure_filename
import os

works_bp = Blueprint('works', __name__, template_folder='templates', static_folder='static', static_url_path='admin/static', url_prefix='/admin')

# Works Add Route
@works_bp.route('/works', methods = ['GET','POST'])
def works():
    form = WorksForm()
    works = Works.query.all()
    if request.method == 'POST':
        file = form.w_img.data
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        works = Works(
            w_title = form.w_title.data,
            w_content = form.w_content.data,
            w_url = form.w_url.data,
            w_img = filename
        )
        db.session.add(works)
        db.session.commit()
        return redirect('/admin/works')
    return render_template('admin/works.html', form = form, works = works)

# Works Watch
@works_bp.route('/works/watch/<id>')
def works_watch(id):
    watchWorks = Works.query.get(id)
    return render_template('admin/works_watch.html', watchworks = watchWorks)

# Works Delete Route
@works_bp.route('/works/delete/<id>')
def works_delete(id):
    deleteWorks = Works.query.get(id)
    db.session.delete(deleteWorks)
    db.session.commit()
    return redirect('/admin/works')