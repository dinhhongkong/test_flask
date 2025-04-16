from flask import Flask
from app.config import Config
from app.extensions import db, ma  # 👈 lấy db từ extensions
from app.controllers.city_controller import city_bp
# from app.controllers.city_controller import city_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)
    # app.register_blueprint(city_bp, url_prefix='/api')
    app.register_blueprint(city_bp)

    return app
