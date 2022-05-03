# Data Container class for CoinMarketCap coin data
import datetime



class cmcCoin:
    def __init__(self, cid, name, symbol, rank, price_usd, price_btc, volusd24h, marketcapusd,
                 available_supply, total_supply, max_supply, change1h, change24h, change7d,
                 last_updated, price_gbp, volgbp24h, marketcapgbp): # initialize   
        self.Id = cid
        self.Name = name
        self.Symbol = symbol # by declaring self.var makes this global 
        self.Rank = rank
        self.PriceGBP = price_gbp
        self.VolumeGBP = volgbp24h
        self.MarketCapGBP = marketcapgbp
        self.PriceUSD = price_usd
        self.VolumeUSD = volusd24h
        self.MarketCapUSD = marketcapusd
        self.PriceBTC = price_btc
        self.AvailableSupply = available_supply
        self.TotalSupply = total_supply
        self.MaxSupply = max_supply
        self.ChangeHour = change1h
        self.ChangeDay = change24h
        self.ChangeWeek = change7d
        self.TimeStamp = last_updated

    def printGBP(self):
        dateandtime = str(datetime.datetime.fromtimestamp(int(self.TimeStamp)))
        return dateandtime + "," + self.Symbol + ","  + "$" + self.PriceGBP + "\n"
    def cointoGBP(self):
        dateandtime = str(datetime.datetime.fromtimestamp(int(self.TimeStamp)))
        return self.Symbol + ",£" + self.PriceGBP + "," + "the date is : " + dateandtime + "\n"

    def quickStats(self):
        headr = "rank  , MarketCapGBP  , MaxSupply"
        return headr + "\n" + self.Rank + " , " + self.MarketCapGBP + " , " + self.MaxSupply + "\n"

    def ROC(self):
        headr = "hourlyChange  , dailyChange  , weeklyChange"
        return headr + "\n" + self.ChangeHour + "," + self.ChangeDay + "," + self.ChangeWeek + "\n"


    def tostring(self):    # method/functions 
        retstr = "Rank,Id,Name,Symbol,PriceGBP,VolumeGBP,MarketCapGBP,PriceUSD,VolumeUSD,MarketCapUSD,PriceBTC"  
        retstr += ",AvailableSupply,TotalSupply,MaxSupply,ChangeHour,ChangeDay,ChangeWeek,TimeStamp\r\n"  # headr string
        retstr += self.tocommas() #automatically calls the next function (tocommas) so that data is included
        return retstr
               


    def tocommas(self): 
        dateandtime = str(datetime.datetime.fromtimestamp(int(self.TimeStamp)))
        return(self.Rank + "," + self.Id + "," + self.Name + "," + self.Symbol + "," + self.PriceGBP
               + "," + self.VolumeGBP + "," + self.MarketCapGBP + "," + self.PriceUSD + "," + self.VolumeUSD
               + "," + self.MarketCapUSD + "," + self.PriceBTC + "," + self.AvailableSupply + "," +
               self.TotalSupply + "," + self.MaxSupply + "," + self.ChangeHour + "," + self.ChangeDay + ","
               + self.ChangeWeek + "," + dateandtime + "\r\n")
