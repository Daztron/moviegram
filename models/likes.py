from db import db

class LikeModel(db.model):
    __tablename__ = "likes"

    l_id = db.Column(db.Integer, primary_key=True)
    u_id = db.Column(db.Integer)
    p_id = db.Column(db.Integer)
    timestamp = db.Column(db.String(128))

    def __init__(self,u_id,p_id,timestamp):
        self.u_id = u_id
        self.p_id = p_id
        self.timestamp = timestamp
    
    def add_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()