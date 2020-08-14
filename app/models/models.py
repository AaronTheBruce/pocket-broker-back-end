from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from datetime import datetime
import json
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String(50), nullable=False)
  last_name = db.Column(db.String(50), nullable=False)
  email = db.Column(db.String(100), unique=True, nullable=False)
  phone_number = db.Column(db.String(20), unique=True, nullable=False)
  hashed_password = db.Column(db.String(100), nullable=False)

  @property
  def password(self):
    return self.hashed_password

  @password.setter
  def password(self, password):
    self.hashed_password = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password, password)

  def __repr__(self):
    return f'User with {self.email} and {self.password}'

  def to_dictionary(self):
    return {
      "first_name": self.first_name,
      "last_name": self.last_name,
      "email": self.email,
      "phone_number": self.phone_number,
    }

class Watch_List_Item(db.Model):
  __tablename__ = "watch_list_items"

  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  crypto_id = db.Column(db.Integer, db.ForeignKey('cryptos.id'), nullable=False)

  def to_dictionary(self):
    return {
      "id": self.id,
      "user_id": self.user_id,
      "crypto_id": self.crypto_id,
    }

  users = db.relationship("User", backref="watch_list_item", lazy=True)
  cryptos = db.relationship("Crypto", backref="watch_list_item", lazy=True)

class Crypto(db.Model):
  __tablename__ = "cryptos"

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(25), nullable=False)
  symbol = db.Column(db.String(3), nullable=False)

class Event_Config(db.Model):
  __tablename__ = "event_configs"

  id = db.Column(db.Integer, primary_key=True)
  start_time = db.Column(db.DateTime, nullable=False)
  end_time = db.Column(db.DateTime, nullable=False)
  percent_change = db.Column(db.Float, nullable=False)
  crypto_id = db.Column(db.Integer, db.ForeignKey('cryptos.id'), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

  cryptos = db.relationship("Crypto", backref='event_config', lazy=True)
  users = db.relationship("User", backref='event_config', lazy=True)

  def to_dictionary(self):
    return {
      "id": self.id,
      "start_time": json.dumps(self.start_time.__str__()),
      "end_time": json.dumps(self.end_time.__str__()),
      "percent_change": self.percent_change,
      "crypto_id": self.crypto_id,
      "user_id": self.user_id,
    }

class Event(db.Model):
  __tablename__ = "events"

  id = db.Column(db.Integer, primary_key=True)
  start_price = db.Column(db.Float, nullable=False)
  end_price = db.Column(db.Float, nullable=False)
  event_config_id = db.Column(db.Integer, db.ForeignKey('event_configs.id'), nullable=False)

  event_configs = db.relationship('Event_Config', backref='event', lazy=True)

  def to_dictionary(self):
    return {
      "start_price": self.start_price,
      "end_price": self.end_price,
      "event_config_id": self.event_config_id,
    }

class Notification(db.Model):
  __tablename__ = "notifications"

  id = db.Column(db.Integer, primary_key=True)
  description = db.Column(db.Text, nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)

  users = db.relationship('User', backref='notification', lazy=True)
  events = db.relationship('Event', backref='notification', lazy=True)

  def to_dictionary(self):
    return {
      "id": self.id,
      "description": self.description,
      "user_id": self.user_id,
      "event_id": self.event_id,
    }
