import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir   =     os.path.abspath(os.path.dirname(__file__))

app       =     Flask(__name__)

app.config['SQLALCHEMY_DATABSE_URI']        =   'sqlite:///'+os.path.join(basedir+'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATION'] =   False

db  =   SQLAlchemy(app)
Migrate(app,db)

class Technology(db.Model):
    __tablename__   =   'Tech'

    id_     =   db.Column(db.Integer,primary_key=True,)
    name    =   db.Column(db.Text)s
    lang    =   db.relationship('Lang',backref='tech',lazy='dynamic')

    owner   =   db.relationship('Owner',backref='tech',uselist=False)

    def __init__(self,name):
        self.name   =   name

    def __repr__(self):
        if self.owner:
            return f"Technoogy name is {self.name} and owner name is {self.Owner.name}"
        else:
            return f"Technology name is {self.name} and has no owner "


class Lang(db.Model):
    __tablename__   =   'lang'

    lang_id     =   db.Column(db.Integer,primary_key=True)
    name        =   db.Column(db.Text)
    Tech_id     =   db.Column(db.Integer,db.ForeignKey('Tech.id_'))

    def __init__(self,name,Tech_id):
        self.name=name
        self.Tech_id=Tech_id


class Owner(db.Model):
    pass