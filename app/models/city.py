from app import db

from datetime import datetime

class City(db.Model):
    __tablename__ = 'city'
    
    city_id = db.Column(db.SmallInteger, primary_key=True, autoincrement=True)
    city = db.Column(db.String(50), nullable=False)
    # country_id = db.Column(db.SmallInteger, db.ForeignKey('country.country_id'), nullable=False)
    country_id = db.Column(db.SmallInteger, nullable=False)
    last_update = db.Column(db.TIMESTAMP, nullable=False)
