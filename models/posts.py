from db import db

class PostModel(db.model):
    __tablename__ = "posts"

    p_id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(32))
    u_id = db.Column(db.Integer)
    timestamp = db.Column(db.String(128))

    def __init__(self,u_id,content,timestamp):
        self.u_id = u_id
        self.content = content
        self.timestamp = timestamp
    
    def add_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()