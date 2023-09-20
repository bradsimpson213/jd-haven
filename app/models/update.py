from .db import db 


class LastUpdate(db.Model):
    __tablename__ = 'lastupdates'
    id = db.Column(db.Integer,  primary_key=True)
    last_update = db.Column(db.DateTime)