from app.models.models import db, User, Event, Notification
from flask_restx import Resource, Namespace, fields

api = Namespace('notifications', description='Create and Destroy Notification')

model = api.model("Notification", {
  "description": fields.String(required=True, description="Notification Description"),
  "user_id": fields.Integer(required=True, description="Identifier for User"),
  "event_id": fields.Integer(required=True, description="Identifier for Event"),
})

@api.route("/")
@api.response(404, 'Notification Not Found')
@api.param('user_id', 'The User Identifier')
class NotificationByUser(Resource):
  def get(self, user_id):
    # get all Notifications for a given user
    notif_by_user = Notification.query.filter_by(user_id=user_id).all()
    data = [notif.to_dictionary() for notif in notif_by_user]
    print("Data", data)
    if notif_by_user:
      return {"data": data}, 201
    return {"message": "Notification Not Found"}, 404

@api.route("/<int:notification_id>")
@api.response(404, 'Notification Not Found')
@api.param('user_id', 'The User Identifier')
@api.param('notification_id', 'The Notification Identifier')
class NotificationByUserAndNotificationId(Resource):
  def delete(self, user_id, notification_id):
    # delete notification by an id
    notif = Notification.query.filter_by(id=notification_id, user_id=user_id).one().to_dictionary()
    if notif['user_id'] == user_id and notif['id'] == notification_id:
      db.session.delete(notif)
      db.session.commit()
      return {"message": "Notification Removed"}, 200
    return {"message": "Notification not found"}, 404
