# API Interface for CoinMarketCap.com
# Python Dependencies
# jenkins exposes the workspace directory through env.
import sys
import os
print(sys.executable)
import json
import urllib.request
#Self Dependencies
import cmccoin


"""


THIS JOB CONNECTS TO COINMARKET CAP, AND PULLS DOWN PRICE DATA FOR EACH COIN AND SAVES TO REPORTS FOLDER

"""

def getAPIdata():   # returns json from url req
    requrl = "https://api.coinmarketcap.com/v1/ticker/?convert=GBP"
    response = urllib.request.urlopen(requrl).read()
    data = response.decode('utf-8')
    jsondata = json.loads(data)
    return jsondata

coins = []
print("Fetching API Data from https://api.coinmarketcap.com ...")
apidata = getAPIdata()
print("Data retreived, filling coin objects")
if "error" not in apidata:  # apidata is a json OBJECT  (we don't need to construct this)
    for item in apidata:   # iterate thru JSON object
        cid = str(item.get("id")) # id is reserved word so use cid
        name = str(item.get("name"))
        symbol = str(item.get("symbol"))
        rank = str(item.get("rank"))
        price_usd = str(item.get("price_usd"))
        price_btc = str(item.get("price_btc"))
        volusd24h = str(item.get("24h_volume_usd"))
        marketcapusd = str(item.get("market_cap_usd"))
        available_supply = str(item.get("available_supply"))
        total_supply = str(item.get("total_supply"))
        max_supply = str(item.get("max_supply"))
        change1h = str(item.get("percent_change_1h"))
        change24h = str(item.get("percent_change_24h"))
        change7d = str(item.get("percent_change_7d"))
        last_updated = str(item.get("last_updated"))
        price_gbp = str(item.get("price_gbp"))
        volgbp24h = str(item.get("24h_volume_gbp"))
        marketcapgbp = str(item.get("market_cap_gbp"))
        tmpCoin = cmccoin.cmcCoin(cid, name, symbol, rank, price_usd, price_btc, volusd24h, marketcapusd,
                                  available_supply, total_supply, max_supply, change1h, change24h, change7d,
                                  last_updated, price_gbp, volgbp24h, marketcapgbp)    # THIS IS CREATION OF OBJECT, CONSTRUCTING (POPULATION)
        coins.append(tmpCoin)
else:
    print("API Returned Error!!")
print("Coin Objects Filled! Iterate and Print")
# An example of coin data access
# coin.tocommas() is also available for a headerless printout
#["BTC", "DOGE", "LTC", "ETH", "ETN", "USDT", "DASH", "ZEC"]
selectedCoins = ["BTC", "DOGE", "LTC", "ETH", "ETN", "USDT", "DASH", "ZEC", "XRP", "BTG", "QTUM", "XEM"]

for coin in coins:
    if coin.Symbol in selectedCoins: # everytime its in this list we use coin.sth
        print(coin.printGBP())


        filename = "/Users/adammcmurchie/projects/Jenkins-Stuff/coinmarketprivate/reports/" + str(coin.Symbol) +"-gbpReport.txt"

        if os.path.exists(filename):
            f = open(filename,'a') # append 
            f.write(str(coin.printGBP()))

        else:
            f = open(filename,'w')
            f.write(str(coin.printGBP()))

        f.close()





        
