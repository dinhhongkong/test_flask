from app import db
from app.models.city import City

class CityRepository:
    @staticmethod
    def get_all_city():
        return City.query.all()
