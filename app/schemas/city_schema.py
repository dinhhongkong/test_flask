from app import ma

from datetime import datetime
from app.models.city import City
class CitySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = City
        include_fk = True  # Bao gồm cả foreign keys

city_schema = CitySchema(many=True)  # Cho nhiều bản ghi