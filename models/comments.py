from db import db

class CommentModel(db.model):
    __tablename__ = "comments"

    c_id = db.Column(db.Integer, primary_key=True)
    u_id = db.Column(db.Integer)
    p_id = db.Column(db.Integer)
    parent_cid = db.Column(db.Integer)
    timestamp = db.Column(db.String(128))

    def __init__(self,u_id,p_id,parent_cid,timestamp):
        self.u_id = u_id
        self.p_id = p_id
        self.parent_cid = parent_cid
        self.timestamp = timestamp
    
    def add_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()