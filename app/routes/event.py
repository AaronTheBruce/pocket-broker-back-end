from app.models.models import db, Event, Event_Config, Crypto
from flask_restx import Resource, Namespace, fields

api = Namespace('events', description='CRUD events')

model = api.model("Event_Config", {
  "start_price": fields.Float(required=True, description="Starting price of event"),
  "end_price": fields.Float(required=True, description="Ending price of event"),
  "event_config_id": fields.Integer(required=True, description="Identifier for User"),
})

@api.route("/")
@api.response(404, 'The Config for this crypto was not found')
@api.param('user_id', 'The User Indentifier')
@api.param('event_config_id', 'The Event Config Indentifier')
class Events(Resource):
  # # get all events for a given event_config
  # def get(self, user_id, event_config_id):
  #   # get all event_configs with the given user_id and config_id
  #   e_config = Event_Config.query.filter_by(user_id=user_id, id=event_config_id).first().to_dictionary()
  #   event_user_id = e_config["user_id"]
  #   events = Event.query.filter_by(event_config_id=event_config_id).all()
  #   e_data = [event.to_dictionary() for event in events]
  #   print("Events", events)
  #   print("Event user id", event_user_id)
  #   if e_config:
  #     print("Data", e_config)
  #     return {"data": data}, 201
  #   return {"message": "Event Config not found"}, 404

  @api.expect(model)
  def post(self, user_id, event_config_id):
    data = api.payload
    if(bool(data)):
      event = {
        "start_price": data["start_price"],
        "end_price": data["end_price"],
        "event_config_id": data["event_config_id"],
      }
      data = Event(**event)
      db.session.add(data)
      db.session.commit()
      return {"message": "Event Saved"}
    return {"message": "Bad Data: Event Not Saved"}


@api.route("/<int:event_id>")
@api.response(404, 'The Config for this crypto was not found')
@api.param('user_id', 'The User Indentifier')
@api.param('event_config_id', 'The Event Config Indentifier')
@api.param('event_id', 'The Event Identifier')
class EventById(Resource):
  # Get event by id
  def get(self, user_id, event_config_id, event_id):
    event = Event.query.filter_by(id=event_id, event_config_id=event_config_id).one().to_dictionary()
    if event:
      return {"event": event}, 201
    return {"message": "Event Not Found"}, 404
