from db import db

class MovieModel(db.model):
    __tablename__ = "movies"
    mv_id = db.Column(db.Integer, primary_key = True)
    mv_name = db.Column(db.String(32), index = True)
    mv_year = db.Column(db.Integer)
    mv_desc = db.Column(db.String(128))
    mv_cast = db.Column(db.String(128))
    mv_imdb_rating = db.Column(db.String(32))

    def __init__(self, mv_name, mv_year, mv_desc, mv_cast, mv_imdb_rating):
        self.mv_name = mv_name
        self.mv_year = mv_year
        self.mv_desc = mv_desc
        self.mv_cast = mv_cast
        self.mv_imdb_rating = mv_imdb_rating
    
    def json(self):
        return {
            "Name": self.mv_name,
            "Description": self.mv_desc,
            "Cast": self.mv_cast,
            "Year": self.mv_year,
            "IMDB Rating": self.mv_imdb_rating
        }
    
    def add_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()