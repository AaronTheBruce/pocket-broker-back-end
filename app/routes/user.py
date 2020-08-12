from app.models.models import db, User
from flask_restx import Resource, Namespace, fields

api = Namespace('users', description='CRUD user')

model = api.model('User', {
  "firstName": fields.String(description="User first name.", example="Bob"),
  "lastName": fields.String(description="User last name.", example="Bobberton"),
  "email": fields.String(description="User Email.", example="bobbadoodle@gmail.com"),
  "phoneNumber": fields.Integer(description="User phone number", example="8608675309"),
  "password": fields.String(description="User password", example="password")
})

@api.route("/<int:id>")
@api.param('id', 'User Identifier')
@api.response(404, 'User not found')
class GetUser(Resource):
  @api.response(200, 'User found')
  @api.doc('get_user')
  def get(self, id):
    # Get User By ID
    user = User.query.filter_by(id=id).one()
    if user == None:
      return {"message": "No user found by this id"}, 404
    return {"user": user.to_dictionary()}, 201

# Use case of this app does not allow updating user profile's as I do not find it important right now
