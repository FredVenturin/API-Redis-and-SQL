from flask import Flask
from src.models.redis.settings.connection import RedisConnectionHandler
from src.models.sqlite.settings.connection import SqliteConnectionHandle

redis_connection_handler = RedisConnectionHandler()
sqlite_connection_handler = SqliteConnectionHandle()

redis_connection_handler.connect()
sqlite_connection_handler.connect()

app = Flask(__name__)

from src.main.routes.products_routes import product_routes_bp

app.register_blueprint(product_routes_bp)