
from libraries import *
from crypto_functions import *

import matplotlib.pyplot as plt



def search_crypto(cryptos):

	search = input('Enter cryptocurrency to display info: ')
	for item in cryptos:
		if item.get('symbol') == search:
			print(item.get('name'))
			print(item.get('current_price'))

			input()
			

def generate_sparklines(cryptos, path):
	folder = 'sparklines'
	neon_pink = '#ff07db'
	neon_cyan = '#00fefc'

	for item in cryptos:

		sparkline = item.get('sparkline')
		if sparkline is not None:
			if sparkline[0] < sparkline[-1]:
				plt.plot(sparkline, neon_cyan)
			else:
				plt.plot(sparkline, neon_pink)

			plt.axis('off')
			filename = item.get('symbol') + '.png'
			destination = "{}/".format(folder) + filename
			plt.savefig(destination, transparent=True)
			plt.clf()
		print(item.get('id'))


def update_watchlist():
	with open('watchlist.txt', 'r') as file:
		watchlist = json.load(file)
	with open('blacklist.txt', 'r') as file:
		blacklist = json.load(file)
	return watchlist, blacklist

def watchlist_creator(cryptos, watchlist, blacklist):
	for coin in cryptos:
		print(coin.get('name') + "({})".format(coin.get('symbol')))
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
		print(item.get('name') + ' ' + "({})".format(item.get('symbol').upper()))
		print('Rank: ' + str(item.get('rank')))
		print('Market Cap: ' + "{:,.0f}".format(item.get('market_cap')))
		print('Dominance: ' + "{:.2f}".format(item.get('dominance')))
		print('')
	input()



def main():
	my_path = os.path.abspath(__file__)

	os.system('clear')
	#list of crypto dictionary objects
	market_data = global_crypto()
	cryptos = update_cryptos(market_data)
	save_json(cryptos, 'cryptosJSON.txt')
	


	#Parameters
	stablecoins = ['wbtc', 'cusdc', 'ausdc', 'usdt', 'ampl', 'dai', 'eosdt', 'dusd', 'dgx', 'esd', 'susd', 'tusd', 'pbtc', 'pax']
	watchlist, blacklist = update_watchlist()
	#def update_watchlist():
	with open('watchlist.txt', 'r') as file:
		watchlist = json.load(file)
	with open('blacklist.txt', 'r') as file:
		blacklist = json.load(file)
	blacklist = blacklist + stablecoins






	menu = True
	while (menu):
		os.system('clear')

		print('Market Cap: ' + "{:,.0f}".format(market_data.get('data').get('total_market_cap').get('usd')))
		print('Change: ' + "{:.2f}".format(market_data.get('data').get('market_cap_change_percentage_24h_usd')))

		print('24h Volume: ' + "{:,.0f}".format(market_data.get('data').get('total_volume').get('usd')))
		print('')

		

		header_title('CryptoVizor', 'All-In-One Cryptocurrency Tracker')
		print('1. Search Cryptocurrency')
		print('2. Watchlist/Blacklist')
		print('3. Show coins')
		print('4. Generate Sparklines')


		print('')
		print('11. View All Time Highs')
		print('4. Dominance Simulator')
		print('5. Plot Sparklines')

		print()
		print('7. Create Crypto List')
		print()
		print('8. Update Crypto List - Quick')
		print('9. Update Crypto List - Hourly')

		print()
		print('0. Exit Program')
		print()




		select = input('Select an option: ')
		os.system('clear')
		if(select == '1'):
			search_crypto(cryptos)
		elif(select == '2'):
			watchlist_creator(cryptos, watchlist, blacklist)

		elif(select == '3'):
			list_coins(cryptos)
		elif(select == '4'):
			list_coins(generate_sparklines(cryptos, my_path))



		elif(select == '11'):
			ath_profit(cryptos, blacklist)

		elif(select == '5'):
			sparkline_plot()
		elif(select == '7'):
			create_cryptos()
		elif(select == '8'):
			update_cryptos(market_data)
		elif(select == '9'):
			create_cryptos()


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









