__author__ = "Kevin-Roberts"

from trader import Trader, CoinOrder


def main():
	api_key = None
	OAUTH2_TEMP = None
	# Edit this value with your api_key or oauth2credenial, uncomment the one you choose to use
	# api_key = "longcharacterstring of api_key given by coinbase"
	# OAUTH2_TEMP ='''{"_module": "oauth2client.client", "token_expiry": "2013-03-31T22:48:20Z", "access_token": "c15a9f84e471db9b0b8fb94f3cb83f08867b4e00cb823f49ead771e928af5c79", "token_uri": "https://www.coinbase.com/oauth/token", "invalid": false, "token_response": {"access_token": "c15a9f84e471db9b0b8fb94f3cb83f08867b4e00cb823f49ead771e928af5c79", "token_type": "bearer", "expires_in": 7200, "refresh_token": "90cb2424ddc39f6668da41a7b46dfd5a729ac9030e19e05fd95bb1880ad07e65", "scope": "all"}, "client_id": "2df06cb383f4ffffac20e257244708c78a1150d128f37d420f11fdc069a914fc", "id_token": null, "client_secret": "7caedd79052d7e29aa0f2700980247e499ce85381e70e4a44de0c08f25bded8a", "revoke_uri": "https://accounts.google.com/o/oauth2/revoke", "_class": "OAuth2Credentials", "refresh_token": "90cb2424ddc39f6668da41a7b46dfd5a729ac9030e19e05fd95bb1880ad07e65", "user_agent": null}'''

	if raw_input("Do you want to try to execute trades? Type 'YES':") == 'YES':
		# IF VALID CREDENTIALS THESE TRADES WILL ATTEMPT TO EXECUTE BE CAREFUL!!!
		myTrader = Trader(api_key = api_key, oauth2_credentials = OAUTH2_TEMP)
		print 'Sell no lower than 1500 usd/btc'
		myTrader.setLimitSell(qty= 0.3, price =1500)
		print 'Buy no higher than 500 usd/btc'
		myTrader.setLimitBuy(qty = 0.2, price = 500)
		print 'Sell if the price drops 10% from the max value seen by .trade()'
		myTrader.setTrailStopLossPercent(qty = 0.3, changeval = 10)

		print 'Start attempting to execute the orders with .trade'
		myTrader.trade(sleeptime = 60)
	else:
		print "if thats the case I suggest you enter in values that won't execute or attempt to sell"
		print "if you sell and don't have coins coinbase will return an error and the trade won't be executed"


if __name__ == "__main__":
	main()