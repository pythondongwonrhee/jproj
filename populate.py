from dbModel import db
# db.create_all()
db.session.rollback()
