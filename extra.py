
#Redirect output to 
#sys.stdout = open('output.txt', 'w')

import importlib
coingecko = ('coingecko_api')
importlib.import_module(coingecko)







def crypto_desc(cryptos):
	for item in cryptos:
		coin = item.get('id')
		if (coin == 'bitcoin'):
			cryptocurrency_api_url = 'https://api.coingecko.com/api/v3/coins/' + coin + '?tickers=true&market_data=true&community_data=true&developer_data=true&sparkline=true'
			r_crypto = requests.get(cryptocurrency_api_url)   
			coin_dict = r_crypto.json()
			description = coin_dict.get('description').get('en')
			item['description'] = description
		#print(next(item for item in cryptos if item["id"] == coin))














#Trending API call
def get_trending():
	trending_list = []
	r = requests.get('https://api.coingecko.com/api/v3/search/trending')
	r_dict = r.json()

	for item in r_dict.get('coins'):
		coin = item.get('item')
		trending_list.append(coin)
	return trending_list






















