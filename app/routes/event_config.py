from app.models.models import db, User, Crypto, Event_Config
from flask_restx import Resource, Namespace, fields

api = Namespace('event_configs', description='CRUD event_config')

model = api.model("Event_Config", {
  "start_date": fields.DateTime(required=True, description="Start time of event"),
  "end_date": fields.DateTime(required=True, description="End time of event"),
  "percent_change": fields.Float(required=True, description="Percent change of event"),
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
      return {"message": f"Success: {data}"}, 201
    return {"message": "Event Configuration Not Found"}, 404

@api.route("/<int:crypto_id>")
@api.param('user_id', 'The User Identifier')
@api.param('crypto_id', 'The Crypto Identifier')
class Event_Config_By_Id(Resource):
  @api.expect(model)
  def post(self, user_id, crypto_id):
    # Post an Event Configuration
    data = api.payload
    if bool(data):
      event_config_data = {
        "start_date": data["start_date"],
        "end_date": data["end_date"],
        "percent_change": data["percent_change"],
        "crypto_id": data["crypto_id"],
        "user_id": data["user_id"],
      }
      data = Event_Config(**event_config_data)
      db.session.add(data)
      db.session.commit()
      return {"message": "Successfully Configured Event!"}
    return {"message": "Bad Data, Event Not Configured..."}
