from flask import Blueprint, request, jsonify
from app.schemas.city_schema import city_schema
from app.services.city_service import CityService

city_bp  = Blueprint('city',__name__)

@city_bp.route('/get_all_city', methods=['GET'])
def get_all_city():
    cities = CityService.list_cities()
    # cities_data = [{
    #     'city_id': city.city_id,
    #     'city': city.city,
    #     'country_id': city.country_id,
    #     'last_update': city.last_update.isoformat() if city.last_update else None
    # } for city in cities]
    
    return jsonify({
        'data': city_schema.dump(cities)
    })

@city_bp.route('/ping', methods=['GET'])
def ping():
    return jsonify({
        'data': "oke"
    })

