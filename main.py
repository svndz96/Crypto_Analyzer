
from libraries import *
from crypto_functions import *
import plotly.express as px

import dateutil.parser as dp

def search_crypto(cryptos, search):
	for item in cryptos:
		if item.get('symbol') == search:
			print(item.get('name'))
			print(item.get('current_price'))
			input()
			



def update_watchlist():
	with open('watchlist.txt', 'r') as file:
		watchlist = json.load(file)
	with open('blacklist.txt', 'r') as file:
		blacklist = json.load(file)
	return watchlist, blacklist



def watchlist_creator(cryptos, watchlist, blacklist):
	for coin in cryptos:
		crypto_info(coin)
		print('W. Add to Watchlist')
		print('B. Add to Blacklist')
		print('Q. Quit')
		select = input('Select an Option: ')
		if select == 'W':
			watchlist.append(coin.get('symbol'))
		elif select == 'B':
			blacklist.append(coin.get('symbol'))
		elif select == 'Q':
			break
		os.system('clear')
	watchlist_json = json.dumps(watchlist)
	with open('watchlist.txt', 'w') as file:
		file.write(watchlist_json)
	blacklist_json = json.dumps(blacklist)
	with open('blacklist.txt', 'w') as file:
		file.write(blacklist_json)


def global_crypto():
	crypto_request = requests.get('https://api.coingecko.com/api/v3/global')
	crypto_dict = crypto_request.json()
	return crypto_dict



def list_coins(cryptos):
	for item in cryptos:
		crypto_info(item)
	input()



def dominance_simulator(cryptos, market):
	market_cap = market.get('market_cap')

	top = 100
	for item in cryptos[:top]:
		crypto_info(item)
		print('Dominance: ' + "{:.2f}".format(item.get('dominance')))
		print('')
	input()




def test(cryptos):
	test = cryptos[0].get('ath_date')
	parsed_t = dp.parse(test)
	t_in_seconds = parsed_t.timestamp()
	print(t_in_seconds)
	input()








def main():
	my_path = os.path.abspath(__file__)

	os.system('clear')
	#list of crypto dictionary objects
	market = global_crypto()
	cryptos = update_cryptos(market)
	cryptos = sorted(cryptos, key=itemgetter('rank'), reverse=False)



	#Parameters
	stablecoins = ['wbtc', 'cusdc', 'ausdc', 'usdt', 'ampl', 'dai', 'eosdt', 'dusd', 'dgx', 'esd', 'susd', 'tusd', 'pbtc', 'pax']
	watchlist, blacklist = update_watchlist()
	blacklist = blacklist + stablecoins
	#vs = get_vs_currencies()
	vs_currency = 'usd'




	#test(cryptos)






	menu = True
	while (menu):
		os.system('clear')


		market_info(market)
		

		header_title('CryptoVizor', 'All-In-One Cryptocurrency Tracker')
		print('1. Search Cryptocurrency')
		print('2. Watchlist/Blacklist')
		print('3. Show coins')
		print('4. Generate Sparklines')
		print('5. Dominance Simulator')
		print('6. Biggest Movers')




		print('7. Search Date')
		print('11. View All Time Highs')

		print()
		print('0. Exit Program')
		print()



		select = input('Select an option: ')
		os.system('clear')


		if(select == '1'):
			search = input('Enter cryptocurrency to display info: ')
			search_crypto(cryptos, search)



		elif(select == '2'):
			watchlist_creator(cryptos, watchlist, blacklist)

		elif(select == '3'):
			list_coins(cryptos)
		
		
	
		elif(select == '4'):
			for item in cryptos:
				generate_sparklines(item)
				print(item.get('id'))

		elif(select == '5'):
			dominance_simulator(cryptos, market)

		elif(select == '6'):
			top_movers(cryptos, market)
	
		elif(select == '11'):
			ath_profit(cryptos, blacklist)



		elif(select == '0'):
			menu = False
		else:
			print('Invalid selection')


































if __name__ == "__main__":
    main()








#Make crypto profile layout
#Long term updates (< weekly)
	#Description, consensus method, hard data, etc
#Mid term updates (hourly < daily < weekly)
	#supply, status updates, market data
#Short term updates (minutes < hourly)
	#Real time price, breaking news









