from app.models.models import db, User, Crypto, Watch_List_Item
from flask_restx import Resource, Namespace, fields

api = Namespace('watch_list_items', description='CRUD watch_list_items')

model = api.model("Watch_List_Item", {
  "crypto_id": fields.Integer(required=True, description="Watch List Item crypto id"),
  "user_id": fields.Integer(required=True, description="Watch List Item user id"),
})

@api.route("/<int:user_id>")
@api.response(404, 'Watch List Item Not Found')
@api.param('user_id', 'The User Identifier')
class Watch_List_Items(Resource):
  # Get all the User's Watch List Items
  def get(self, user_id):
    # Get all the Watch List Items for a User
    wl_items = Watch_List_Item.query.filter_by(user_id=user_id).all()
    if wl_items == None:
      return {"message": "No Items Found"}, 404
    return {"item": wl_items.to_dictionary()}, 201

  @api.expect(model)
  def post(self, user_id):
    # Post a crypto to a user
    # print("API payload", api.payload)
    data = api.payload
    if bool(data):
      watch_list_data = {
        "crypto_id": int(data["crypto_id"]),
        "user_id": int(data["user_id"]),
      }
    # print("Watch List Data", watch_list_data)
      item = Watch_List_Item(**watch_list_data)
      db.session.add(item)
      db.session.commit()
      return {"message": "Successfully added item to Watch List!"}
    return { "message": "Bad Data" }


    # user = User.query.filter_by(id=user_id).first()
    # crypto = Crypto.query.filter_by(id=crypto_id).first()
    # if(bool(user) and bool(crypto)):
    #   print("New Item", new_item)

    # watch_list_item = Watch_List_Item(**new_item)
    # db.session.add(watch_list_item)
    # db.session.commit()
    # print("Watch List Item", watch_list_item)
    # return { "data": data["watch_list_item"].to_dictionary() }
