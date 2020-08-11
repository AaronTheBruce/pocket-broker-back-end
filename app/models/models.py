from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from datetime import datetime
import json
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  first_name_ = db.Column(db.String(50), nullable=False)
  last_name = db.Column(db.String(50), nullable=False)
  email = db.Column(db.string(100), unique=True, nullable=False)
  phone_number = db.Column(db.Integer, unique=True nullable=False)
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

  watch_list_items = db.relationship("watch_list_items", backref="user", lazy=True)
  notifications = db.relationship("notifications", backref="user", lazy=True)
  event_configs = db.relationship("event_configs", backref="user", lazy=True)

class Watch_List_Items(db.Model):
  __tablename__ = "watch_list_items"

  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
  crypto_id = db.Column(db.Integer, db.ForeignKey('cryptos.id'), nullable=False)

  def to_dictionary(self):
    return {
      "user_first_name": self.user.first_name,
      "user_last_name": self.user.last_name,
      "crypto_name": self.crypto.name,
    }

class Crypto(db.Model):
  __tablename__ = "cryptos"

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(25), nullable=False)

  Watch_List_Items = db.relationship("Watch_List_Item", backref="crypto", lazy=True)
  Event_Configs = db.relationship("Event_Config", backref="crypto", lazy=True)

class Event_Config(db.Model):
  __tablename__ = "event_configs"

  id = db.Column(db.Integer, primary_key=True)
  start_date = db.Column(db.Datetime, nullable=False)
  end_date = db.Column(db.Datetime, nullable=False)
  percent_change = db.Column(db.Numeric, nullable=False)
  crypto_id = db.Column(db.Integer, db.ForeignKey('cryptos.id'), nullable=False)
  users_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

  events = db.relationship('Event', backref='event_config', lazy=True)

class Event(db.Model):
  __tablename__ = "events"

  id = db.Column(db.Integer, primary_key=True)
  start_price = db.Column(db.Float, nullable=False)
  end_price = db.Column(db.Float, nullable=False)

  Event_Configs = db.relationship('Event_Config', backref='notification', lazy=True)
