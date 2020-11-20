from app import db

class Gifter(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    email = db.Column(db.String(120))
    giftee = db.relationship('Giftee', backref='gift_owner', lazy='dynamic')

    def __repr__(self):
        return '<Gifter {} {}>'.format(self.id, self.email)
        
class Giftee(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    first_name = db.Column(db.String(120))
    last_name = db.Column(db.String(120))
    email = db.Column(db.String(120))
    personal_note = db.Column(db.Text())
    send_gift_date = db.Column(db.Date())
    gifter_id = db.Column(db.Integer, db.ForeignKey('gifter.id'))

    def __repr__(self):
        return '<Gifter {} {}>'.format(self.id, self.email)
 

class StripeCheckoutSession(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False, autoincrement=True)
    session_id = db.Column(db.String(120))
    gifter_id = db.Column(db.Integer, db.ForeignKey('gifter.id'))

    def __repr__(self):
        return '<StripeCheckoutSession {} {}>'.format(self.id, self.session_id)