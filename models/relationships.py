from db import db

class RelationshipModel(db.model):
    __tablename__ = "relationships"

    r_id = db.Column(db.Integer, primary_key=True)
    u1_id = db.Column(db.Integer)
    u2_id = db.Column(db.Integer)
    status = db.Column(db.Integer)
    action_user_id = db.Column(db.Integer)
    timestamp = db.Column(db.String(128))

    def __init__(self,u1_id,u2_id,status,action_user_id,timestamp):
        self.u1_id = u1_id
        self.u2_id = u2_id
        # Status can be 
        # 0 - pending
        # 1 - accepted
        # 2 - declined
        # 3 - blocked
        self.status = status
        self.action_user_id = action_user_id
        self.timestamp = timestamp
    
    def update(self,status,action_user_id, timestamp):
        self.status = status
        self.action_user_id = action_user_id
        self.timestamp = timestamp

    def add_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()