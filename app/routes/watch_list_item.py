from app.models.models import db, User, Crypto, Watch_List_Item
from flask_restx import Resource, Namespace, fields

api = Namespace('watch_list_items', description='CRUD watch_list_items')

model = api.model("Watch_List_Item", {
  "crypto_id": fields.Integer(required=True, description="Watch List Item crypto id"),
  "user_id": fields.Integer(required=True, description="Watch List Item user id"),
})

@api.route("/")
@api.response(404, 'User Not Found')
@api.param('user_id', 'The User Identifier')
class Watch_List_Items(Resource):
  # Get all the User's Watch List Items
  def get(self, user_id):
    # Get all the Watch List Items fo a User
    wl_items = Watch_List_Item.query.filter_by(user_id=user_id).all()
    if wl_items == None:
      return {"message": "No Items Found"}, 404
    print(wl_items)
    data = [wl_item.to_dictionary() for wl_item in wl_items]
    return {"items": data}, 201

  @api.expect(model)
  def post(self, user_id):
    # Post a crypto to a user
    data = api.payload
    if bool(data):
      watch_list_data = {
        "crypto_id": int(data["crypto_id"]),
        "user_id": int(data["user_id"]),
      }
      item = Watch_List_Item(**watch_list_data)
      db.session.add(item)
      db.session.commit()
      return {"message": "Successfully added item to Watch List!"}, 200
    return { "message": "Bad Data Provided" }, 400

@api.route("/<int:crypto_id>")
@api.response(404, 'Crypto Not Found')
@api.param('user_id', 'The User Identifier')
@api.param('crypto_id', 'The Crypto Identifier')
class Watch_List_Items_By_Id(Resource):
  def get(self, user_id, crypto_id):
    data = api.payload
    wl_item = Watch_List_Item.query.filter_by(user_id=user_id, crypto_id=crypto_id).first().to_dictionary()
    if wl_item == None :
      return {"message": "Watch List Item Not FOund"}, 404
    return {"message": f"Success: {wl_item}"}

  def delete(self, user_id, crypto_id):
    # Delete an item from watchlist
    wl_item = Watch_List_Item.query.filter_by(user_id=user_id, crypto_id=crypto_id).one().to_dictionary()
    # Make damn sure it's the right item
    if wl_item['user_id'] == user_id and wl_item['crypto_id'] == crypto_id:
      db.session.delete(wl_item)
      db.session.commit()
      return {"message": "Watch Item Successfully Removed"}, 200
    return {"message": "Watch Item Not Found, nothing deleted"}, 404
