# App / 'models.py'
from app import db

class Services(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    icon = db.Column(db.String(255))

class Works(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    w_title = db.Column(db.String(255))
    w_content = db.Column(db.String(255))
    w_url = db.Column(db.String(255))
    w_img = db.Column(db.String(255))

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    c_img = db.Column(db.String(255))

class Latest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    l_title = db.Column(db.String(255))
    l_url = db.Column(db.String(255))
    l_content = db.Column(db.Text)
    l_img = db.Column(db.String(255))




