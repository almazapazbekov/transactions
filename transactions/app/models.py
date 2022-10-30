from . import db


class Transactions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.Integer)
    status = db.Column(db.String(10))
    unit = db.Column(db.String(10))
    comment = db.Column(db.String(10))

    def __repr__(self):
        return self.name



