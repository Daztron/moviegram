from db import db

class RatingModel(db.Model):
    __tablename__ = "ratings"
    r_id = db.Column(db.Integer, primary_key = True)
    u_id = db.Column(db.Integer)
    mv_id = db.Column(db.Integer)
    mv_rating = db.Column(db.Integer)
    mv_review = db.Column(db.String(128))

    def __init__(self, u_id, mv_id, mv_rating, mv_review):
        self.u_id = u_id
        self.mv_id = mv_id
        self.mv_rating = mv_rating
        self.mv_review = mv_review

    def add_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()