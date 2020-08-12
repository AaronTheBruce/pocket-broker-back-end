from app.models.models import db, Crypto
from flask_restx import Resource, Namespace, fields

api = Namespace('cryptos', description='Get crypto cryptocurrencies')

model = api.model("Crypto", {
  "name": fields.String(description="Crypto name", example="Bitcoin"),
  "symbol": fields.String(description="Crypto symbol", example="BTC"),
})

@api.route("/<int:id>")
@api.param('id', 'Crypto identifier')
@api.response(404, 'Crypto not found')
class GetCrypto(Resource):
  @api.response(200, 'Crypto Found')
  @api.doc('get_crypto')
  def get(self, id):
    # Get crypto by id
    crypto = Crypto.query.filter_by(id=id).first()
    if crypto == None:
      return {"message": "No Crypto found by that id"}, 404
    return {"crypto": crypto.to_dictionary()}, 201

# User is not meant to create update or destroy cryptos.
# Only Get is supported here, as the supported cryptos will be seeded
