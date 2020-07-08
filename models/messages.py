from db import db

class MessagesModel(db.model):
    __tablename__ = "messages"

    m_id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer)
    receiver_id = db.Column(db.Integer)
    content = db.Column(db.Integer)
    timestamp = db.Column(db.String(128))

    def __init__(self,sender_id,receiver_id,content,timestamp):
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.content = content
        self.timestamp = timestamp


    def add_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()