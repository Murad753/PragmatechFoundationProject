from flask import Blueprint, render_template, redirect, request, url_for
from app import app, db
from app.models import Client
from admin.forms import ClientForm
from werkzeug.utils import secure_filename
import os
client_bp = Blueprint('client', __name__, template_folder='templates', static_folder='static', static_url_path='admin/static', url_prefix='/admin')

# Client Add Route
@client_bp.route('/client', methods = ['GET','POST'])
def client():
    form = ClientForm()
    client = Client.query.all()
    if request.method == 'POST':
        file = form.c_img.data
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        client = Client(
            c_img = filename
        )
        db.session.add(client)
        db.session.commit()
        return redirect('/admin/client')
    return render_template('admin/client.html', form=form, client = client)

# Client Watch Route
@client_bp.route('/client/watch/<id>')
def client_watch(id):
    watchClient = Client.query.get(id)
    return render_template('admin/client_watch.html', watchClient = watchClient)

# Client Delete Route
@client_bp.route('/client/delete/<id>')
def client_delete(id):
    deleteClient = Client.query.get(id)
    db.session.delete(deleteClient)
    db.session.commit()
    return redirect('/admin/client')