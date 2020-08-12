from dotenv import load_dotenv
load_dotenv()

from app import app, db
from app.models.models import (
  User, Crypto, Watch_List_Item
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
    hashed_password='password',
  )

  crypto1 = Crypto(
    name='Bitcoin',
    symbol='BTC',
  )

  crypto2 = Crypto(
    name='Etherium',
    symbol='ETH'
  )

  crypto3 = Crypto(
    name='LiteCoin',
    symbol='LTC'
  )

  crypto4 = Crypto(
    name='Bitcoin Cash',
    symbol='BCH'
  )

  crypto5 = Crypto(
    name='Ripple',
    symbol='XRP'
  )

  watch_item1 = Watch_List_Item(
    user_id=1,
    crypto_id=1
  )
  watch_item2 = Watch_List_Item(
    user_id=1,
    crypto_id=2
  )
  watch_item3 = Watch_List_Item(
    user_id=1,
    crypto_id=3
  )

  db.session.add(user1)
  db.session.add(crypto1)
  db.session.add(crypto2)
  db.session.add(crypto3)
  db.session.add(crypto4)
  db.session.add(crypto5)
  db.session.add(watch_item1)
  db.session.add(watch_item2)
  db.session.add(watch_item3)
  db.session.commit()
