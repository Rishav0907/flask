import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir=os.path.abspath(os.path.dirname(__file__))

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATION']=False

db=SQLAlchemy(app)
Migrate(app,db)


class Tech(db.Model):
    __tablename__='Tech'

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text)
    age=db.Column(db.Integer)
    stream=db.Column(db.Text)

    def __init__(self,name,age,stream):
        self.name=name
        self.age=age
        self.stream=stream

    def __repr__(self):
        return f"Tech {self.name} and {self.age}"