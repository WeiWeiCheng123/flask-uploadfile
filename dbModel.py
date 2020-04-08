from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://hafvjjloitkhzv:ab31a6e9c4b6bebef026b0ac9f1caf0cf9c18a238b18a40c510ff0d9ac602464@ec2-54-147-209-121.compute-1.amazonaws.com:5432/d3rifa0so0785l'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


class FileContents(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    data = db.Column(db.LargeBinary)

    def __init__(self
                , name
                , data
                ):
         self.name = name
         self.data = 	data

if __name__ == '__main__':
    manager.run()