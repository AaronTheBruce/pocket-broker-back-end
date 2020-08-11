from flask import Blueprint, redirect, url_for, request
from app.models.models import db, User
from flask_jwt_extended import JWTManager, create_access_token
from flask_restx import Resource, Namespace, fields

api = Namespace("auth", description="User authorization")

login_model = api.model(
  "Login",
  {
    "email": fields.String(
      required=True, description="Unique email address.", example="demo@demo.com"
    ),
    "password": fields.String(
      required=True, description="User Password", example="password"
    ),
  },
)

signup_model = api.clone(
  "Signup",
  login_model,
  {
    "firstName": fields.String(
      required=True, description="User first name", example="Bob"
    ),
    "lastName": fields.String(
      required=True, description="User last name", example="Bobbington"
    ),
    "phoneNumber": fields.String(
      required=True, description="User phone number", example="860-867-5309"
    ),
  },
)

@api.route("/signup")
class Signup(Resource):
  @api.doc("signup_user")
  @api.expect(signup_model)
  def post(self):
    # create a user record on a signup
    email = api.payload["email"]
    password = api.payload["password"]

    testaroo = User.query.filter_by(email=email).first()
    if testaroo:
      return {"message": "The email already is registered"}, 409
    else:
      password = api.payload["password"]
      first_name = api.payload["firstName"]
      last_name = api.payload["lastName"]
      phoneNumber = api.payload["phoneNumber"]
      user = User(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password,
        phone_number=phoneNumber,
      )

      db.session.add(user)
      db.session.commit()
      return {"message": "Success! User Created!" }, 201

@api.route("/login")
class Login(Resource):
  @api.expect(login_model)
  def post(self):
    # Get user infor and access token for a login request
    email = api.payload["email"]
    password = api.payload["password"]

    user = User.query.filter_by(email=email).first()

    if user:
      valid = user.check_password(password)
      if valid:
        access_token = create_access_token(identity=email)
        return {
          "access_token": access_token,
          "user_id": user.id,
        }
    else:
      return {"message": "Error: Bad email or password."}, 401
