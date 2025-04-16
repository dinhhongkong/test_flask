import time
from app.repositories.city_repository import CityRepository
from datetime import datetime

class CityService:
    @staticmethod
    def list_cities():
        """Get all cities"""
        return CityRepository.get_all_city()


