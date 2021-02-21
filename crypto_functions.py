from libraries import *


def coingecko_markets_api():
	vs_currency = 'usd'
	order = 'market_cap_desc'
	per_page = '100'
	page = '1'
	sparkline = True
	price_change_percentage = '1h%2C24h%2C7d%2C30d%2C1y'
	
	coingecko_markets_url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=' +vs_currency+ '&order=' +order+ '&per_page=' +per_page+ '&page=' +page+ '&sparkline=' +str(sparkline)+ '&price_change_percentage=' +price_change_percentage
	return coingecko_markets_url


#Creating initial crypto list (id, name, symbol)
def create_cryptos():
	coin_list_request = requests.get('https://api.coingecko.com/api/v3/coins/list')
	coin_list_dict = coin_list_request.json()

	coin_list = []
	for item in coin_list_dict:
		coin_dict = {}
		coin_dict['id'] = item.get('id')
		coin_dict['name'] = item.get('name')
		coin_dict['symbol'] = item.get('symbol')
		coin_list.append(coin_dict)
	save_json(coin_list, 'coin_list.txt')

def update_cryptos_minute():
	crypto_market_request = requests.get(coingecko_markets_api())
	crypto_market_dict = crypto_market_request.json()
	

def update_cryptos(crypto_market):
	crypto_list = []
	r = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h%2C24h%2C7d%2C30d%2C1y')
	r_dict = r.json()

	#values for crypto profile
	for item in r_dict:
		crypto_dict = {}
		#Create once
		crypto_dict['id'] = item.get('id')
		crypto_dict['name'] = item.get('name')
		crypto_dict['symbol'] = item.get('symbol')


		#Update Quickly
		crypto_dict['rank'] = item.get('market_cap_rank')
		crypto_dict['market_cap'] = item.get('market_cap')
		crypto_dict['current_price'] = item.get('current_price')
		crypto_dict['volume_24'] = item.get('total_volume')
		crypto_dict['low_24h'] = item.get('low_24h')
		crypto_dict['high_24h'] = item.get('high_24h')

		crypto_dict['price_change_24h'] = item.get('price_change_24h')
		crypto_dict['price_change_percentage_24h'] = item.get('price_change_percentage_24h')
		crypto_dict['market_cap_change_24h'] = item.get('market_cap_change_24h')
		crypto_dict['market_cap_change_percentage_24h'] = item.get('market_cap_change_percentage_24h')

		#Current market cap divided by total crypto market cap to find percentage of dominance
		crypto_dict['dominance'] = (crypto_dict['market_cap']/crypto_market.get('data').get('total_market_cap').get('usd'))*100


		#Update daily
		crypto_dict['circulating_supply'] = item.get('circulating_supply')
		crypto_dict['total_supply'] = item.get('total_supply')
		crypto_dict['max_supply'] = item.get('max_supply')

		#Update daily
		crypto_dict['ath'] = item.get('ath')
		crypto_dict['ath_change_percentage'] = item.get('ath_change_percentage')
		crypto_dict['ath_date'] = item.get('ath_date')
		crypto_dict['profit_multiplier'] = item.get('ath')/item.get('current_price')
		crypto_dict['sparkline'] = item.get('sparkline_in_7d').get('price')


		crypto_list.append(crypto_dict)
	return crypto_list


def save_json(dicts_list, file_name):
	crypto_json = json.dumps(dicts_list)
	
	json_file = open(file_name,"w")
	json_file.write(crypto_json)
	json_file.close() 
	return crypto_json


def print_json(dicts_list):
	pass


def header_title(title, desc):
	print(title)
	print(desc)
	print('------------------------------')
	print()



def ath_profit(cryptos, blacklist):
	header_title('All-Time-High Profits $$$', 'Show all-time-high data and profit multipliers')
	#Custom/Default parameters
	custom = 0
	if (custom):
		rank = int(input('Enter ranks to include in search: '))
		ath_change = float(input('Enter all time high change percentage: '))
	else:
		rank = 1000
		ath_change = 10

	cryptos_sorted = sorted(cryptos, key=itemgetter('ath_change_percentage'), reverse=True) 
	for item in cryptos_sorted:
		if (abs(item.get('ath_change_percentage')) >= ath_change) & (item.get('rank') <= rank) & (item.get('symbol') not in blacklist):
			print(item.get('name') + ' (' + str(item.get('symbol')).upper() + ')')
			print('Rank: ' + str(item.get('rank')))
			print('Market Cap: ' + "{:,}".format(item.get('market_cap')) + '\t\t24h Volume: ' + "{:,}".format(item.get('volume_24')))
			print('--------------------------------------------------')
			print('Current price: ' + str(item.get('current_price')))
			print('--------------------------------------------------')
			print('All Time High: ' + str(item.get('ath')) + '\tChange: ' + str(item.get('ath_change_percentage')))
			print('Profit Multiplier: ' + "{:.2f}".format(item.get('profit_multiplier')))
			print('Reached ATH on: ' + str(item.get('ath_date')))
			print()
	input('ENTER to continue...')
