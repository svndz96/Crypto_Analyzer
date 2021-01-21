from replit import db
import requests
import json



#Trending API call
def get_trending():
	trending_list = []
	r = requests.get('https://api.coingecko.com/api/v3/search/trending')
	r_dict = r.json()

	for item in r_dict.get('coins'):
		coin = item.get('item')
		trending_list.append(coin)
	return trending_list


#Create crypto profiles
def get_crypto():
	crypto_list = []
	r = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=1&sparkline=true')
	r_dict = r.json()


	#values for crypto profile
	for item in r_dict:
		crypto_dict = {}
		crypto_dict['id'] = item.get('id')
		crypto_dict['name'] = item.get('name')
		crypto_dict['symbol'] = item.get('symbol')
		crypto_dict['rank'] = item.get('market_cap_rank')

		crypto_dict['market_cap'] = item.get('market_cap')
		crypto_dict['current_price'] = item.get('current_price')
		crypto_dict['volume_24'] = item.get('total_volume')
		crypto_dict['low_24'] = item.get('low_24')
		crypto_dict['high_24'] = item.get('high_24')

		crypto_dict['price_change_24h'] = item.get('price_change_24h')
		crypto_dict['price_change_percentage_24h'] = item.get('price_change_percentage_24h')
		crypto_dict['market_cap_change_24h'] = item.get('market_cap_change_24h')
		crypto_dict['market_cap_change_percentage_24h'] = item.get('market_cap_change_percentage_24h')

		crypto_dict['circulating_supply'] = item.get('circulating_supply')
		crypto_dict['total_supply'] = item.get('total_supply')
		crypto_dict['max_supply'] = item.get('max_supply')


		crypto_dict['ath'] = item.get('ath')
		crypto_dict['ath_change_percentage'] = item.get('ath_change_percentage')
		crypto_dict['ath_date'] = item.get('ath_date')

		crypto_list.append(crypto_dict)

	return crypto_list


def convert_dicts_json(dicts_list):
	crypto_json = json.dumps(dicts_list)
	return crypto_json





class crypto:  
    def __init__(self, name):  
        self.name = name  






cryptos = get_crypto()


for item in cryptos:
	coin = item.get('id')

	if (coin == 'bitcoin'):

		cryptocurrency_api_url = 'https://api.coingecko.com/api/v3/coins/' + coin + '?tickers=true&market_data=true&community_data=true&developer_data=true&sparkline=true'
		r_crypto = requests.get(cryptocurrency_api_url)
		coin_dict = r_crypto.json()
		description = coin_dict.get('description').get('en')
		print(description)
		item['description'] = description


	#print(next(item for item in crypto_list if item["id"] == search))


for item in cryptos:
	coin = item.get('id')

	if (coin == 'bitcoin'):
		print(item.get('description'))









#Make crypto profile layout
#Long term updates (< weekly)
	#Description, consensus method, hard data, etc
#Mid term updates (hourly < daily < weekly)
	#supply, status updates, market data
#Short term updates (minutes < hourly)
	#Real time price, breaking news









