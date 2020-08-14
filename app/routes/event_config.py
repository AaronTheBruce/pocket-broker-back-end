from app.models.models import db, User, Crypto, Event_Config
from flask_restx import Resource, Namespace, fields

api = Namespace('event_configs', description='CRUD event_config')

model = api.model("Event_Config", {
  "time_frame": fields.String(required=True, description="Day, Week, Month, Year"),
  "percent_change": fields.Float(required=True, description="Percent change of event"),
  "usd_sell_price": fields.Float(required=False, description="Price willing to sell if met"),
  "usd_buy_price": fields.Float(required=False, description="Price willing to buy if met"),
  "usd_buy_power": fields.Float(required=False, description="US Dollar willing purchase for buy event"),
  "crypto_id": fields.Integer(required=True, description="Identifier for Crypto"),
  "user_id": fields.Integer(required=True, description="Identifier for User"),
})

@api.route("/")
@api.response(404, 'Event Config Not Found')
@api.param('user_id', 'The User Identifier')
class Event_Configs(Resource):
  # Get all the Config's by id
  def get(self, user_id):
    # Get all the Event Configs for a User
    event_configs = Event_Config.query.filter_by(user_id=user_id).all()
    data = [event_config for event_config in event_configs]
    print("Data", data)
    if event_configs:
      return {"data": data}, 201
    return {"message": "Event Configuration Not Found"}, 404

@api.route("/<int:crypto_id>")
@api.param('user_id', 'The User Identifier')
@api.param('crypto_id', 'The Crypto Identifier')
class Event_Config_By_Crypto_Id(Resource):
  @api.expect(model)
  def post(self, user_id, crypto_id):
    # Post an Event Configuration
    data = api.payload
    if bool(data):
      event_config_data = {
        "time_frame": data["time_frame"],
        "percent_change": data["percent_change"],
        "usd_sell_price": data["usd_sell_price"],
        "usd_buy_price": data["usd_buy_price"],
        "usd_buy_power": data["usd_buy_power"],
        "crypto_id": data["crypto_id"],
        "user_id": data["user_id"],
      }
      data = Event_Config(**event_config_data)
      db.session.add(data)
      db.session.commit()
      return {"message": "Successfully Configured Event!"}
    return {"message": "Bad Data, Event Not Configured..."}

@api.route("/<int:event_config_id>")
@api.param('user_id', 'The User Identifier')
# @api.param('crypto_id', 'The Crypto Identifier')
@api.param('event_config_id', 'The Event Config Identifier')
class Event_Config_By_Id(Resource):
  @api.expect(model)
  def put(self, user_id, event_config_id):
    data = api.payload
    e_config = Event_Config.query.filter_by(id=event_config_id, user_id=user_id).one().to_dictionary()
    if e_config:
      e_config = {
        "time_frame": data["time_frame"],
        "percent_change": data["percent_change"],
        "usd_sell_price": data["usd_sell_price"],
        "usd_buy_price": data["usd_buy_price"],
        "usd_buy_power": data["usd_buy_power"],
      }
      data = Event_Config(**e_config)
      db.session.add()
      db.session.commit()
      return {"message": "Successfully Updated Event Config"}
    return {"message": "Bad Data, Event Config Not Updated"}

  def delete(self, user_id, event_config_id):
    # delete event config by id and user id
    e_config = Event_Config.query.filter_by(id=event_config_id, user_id=user_id).one().to_dictionary()
    if e_config['user_id'] == user_id and e_config['id'] == event_config_id:
      db.session.delete(e_config)
      db.session.commit()
      return {"message": "Event Config Deleted"}, 200
    return {"message": "Event Config Not Found"}, 404
