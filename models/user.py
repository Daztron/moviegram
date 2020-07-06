from db import db

class UserModel(db.Model):
    __tablename__ = "users"
    u_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, username):
        self.username = username

    def hash_password(self,password):
        self.password_hash = password + "gkp" # temporary hash
    
    def verify_password(self,password):
        return True if password + "gkp" == self.password_hash else False
    
    def get_username(self):
        return self.username

    @classmethod
    def find_by_uname(cls, username):
        return cls.query.filter_by(username=username).first()
    
    @classmethod
    def find_by_uid(cls, u_id):
        return cls.query.filter_by(u_id=u_id).first()
    
    @classmethod
    def get_usernames(cls):
        return cls.query.all()
    
    
    def add_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
    

