from flask import Flask
from app.config import Configuration
from app.models.models import db
from flask_cors import CORS
from flask_restx import Api
from app.routes.auth import api as auth
# import app.routes.<<file>>


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*", "supports_credentials": True}})

jwt = JWTManager(app)
app.config.from_object(Configuration)
db.init_app(app)

api = Api
