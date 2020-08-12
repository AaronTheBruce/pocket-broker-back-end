from flask import Flask
from flask_jwt_extended import JWTManager
from app.config import Configuration
from app.models.models import db, User
from flask_migrate import Migrate
from flask_cors import CORS
from flask_restx import Api
from app.routes.auth import api as auth
from app.routes.user import api as user
from app.routes.crypto import api as crypto
from app.routes.watch_list_item import api as watch_list_item


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*", "supports_credentials": True}})

jwt = JWTManager(app)
app.config.from_object(Configuration)
db.init_app(app)

api = Api(app)
api.add_namespace(auth)
api.add_namespace(user)
api.add_namespace(crypto)
api.add_namespace(watch_list_item)
Migrate(app, db)
