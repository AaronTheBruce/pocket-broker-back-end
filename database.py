from dotenv import load_dotenv
import datetime
load_dotenv()

from app import app, db
from app.models.models import (
  User, Crypto, Watch_List_Item, Event, Event_Config, Notification
)

with app.app_context():
  db.drop_all()
  db.create_all()

  # 1 user
  # 5 crypto
  # 3 watch_list

  user1 = User(
    first_name='Aaron',
    last_name='Bruce',
    email='aaronbruce555@gmail.com',
    phone_number='2035251846',
    hashed_password='pbkdf2:sha256:150000$DLHLKceX$7fe8491686a2aa0a94216157342e17f5d8083de29443913031e47e50bd14caa3',
  )

  user2 = User(
    first_name='Demo',
    last_name='Demo',
    email='demouser@demo.com',
    phone_number='2038675309',
    hashed_password='pbkdf2:sha256:150000$DLHLKceX$7fe8491686a2aa0a94216157342e17f5d8083de29443913031e47e50bd14caa3',
  )

  crypto1 = Crypto(
    name='bitcoin',
    symbol='BTC',
  )
  crypto2 = Crypto(
    name='ethereum',
    symbol='ETH'
  )
  crypto3 = Crypto(
    name='litecoin',
    symbol='LTC'
  )
  crypto4 = Crypto(
    name='bitcoin-cash',
    symbol='BCH'
  )
  crypto5 = Crypto(
    name='ripple',
    symbol='XRP'
  )
  crypto6 = Crypto(
    name='basic-attention-token',
    symbol='BAT'
  )
  crypto7 = Crypto(
    name='dogecoin',
    symbol='DOGE'
  )
  crypto8 = Crypto(
    name='ethereum-classic',
    symbol='ETC'
  )
  watch_item_1 = Watch_List_Item(
    user_id=1,
    crypto_id=1
  )
  watch_item_2 = Watch_List_Item(
    user_id=1,
    crypto_id=2
  )
  watch_item_3 = Watch_List_Item(
    user_id=1,
    crypto_id=3
  )
  event_config_1 = Event_Config(
    time_frame="Week",
    percent_change=5.0,
    usd_sell_price=20000.0,
    usd_buy_price=9000.0,
    usd_buy_power=50.0,
    crypto_id=1,
    user_id=1,
  )
  event_1 = Event(
    usd_start_price=12000.0,
    usd_end_price=12050.0,
    start_time=datetime.datetime(2020, 8, 5),
    end_time=datetime.datetime(2020, 8, 12),
    event_config_id=1
  )
  notification_1 = Notification(
    description="Test",
    user_id=1,
    event_id=1,
  )
  db.session.add(user1)
  db.session.add(user2)
  db.session.add(crypto1)
  db.session.add(crypto2)
  db.session.add(crypto3)
  db.session.add(crypto4)
  db.session.add(crypto5)
  db.session.add(crypto6)
  db.session.add(crypto7)
  db.session.add(crypto8)
  db.session.add(watch_item_1)
  db.session.add(watch_item_2)
  db.session.add(watch_item_3)
  db.session.add(event_config_1)
  db.session.add(event_1)
  db.session.add(notification_1)
  db.session.commit()
