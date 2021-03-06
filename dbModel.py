from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from sqlalchemy import desc

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:JayY@localhost:5432/postgres'
app.config[
    'SQLALCHEMY_DATABASE_URI'] = 'postgres://gmwmjhrwjmzvfk:89f9419302c69def47cd6b9b8a2412771c42b388d7abfc47127a667b61ae0259@ec2-54-221-236-144.compute-1.amazonaws.com:5432/ddhepk539jd42o'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


class CommentDb(db.Model):
    
    __tablename__ = 'CommentDb'

    Id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(24))
    Comment = db.Column(db.String(300))
    CreateDate = db.Column(db.DateTime)

    def __init__(self
                 , Name
                 , Comment
                 , CreateDate
                 ):
        self.Name = Name
        self.Comment = Comment
        self.CreateDate = CreateDate


if __name__ == '__main__':
    manager.run()
