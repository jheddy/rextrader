import requests
import json
import hmac
import random
import urllib, urllib2
import hashlib

apiVersion='v1.1'
apiUrl='https://bittrex.com/api/'+apiVersion
publicApiUrl=apiUrl+'/public/'
marketApiUrl=apiUrl+'/market/'
accountApiUr=apiUrl+'/account/'

# PUBLIC API
# https://bittrex.com/api/v1.1/public/getmarkets    
# https://bittrex.com/api/v1.1/public/getcurrencies    
# https://bittrex.com/api/v1.1/public/getticker    
# https://bittrex.com/api/v1.1/public/getmarketsummaries    
# https://bittrex.com/api/v1.1/public/getmarketsummary?market=btc-ltc    
# https://bittrex.com/api/v1.1/public/getorderbook?market=BTC-LTC&type=both&depth=50    
# https://bittrex.com/api/v1.1/public/getmarkethistory?market=BTC-DOGE 

##### USE data,params and headers #####

# MARKET API   
# https://bittrex.com/api/v1.1/market/buylimit?apikey=API_KEY&market=BTC-LTC&quantity=1.2&rate=1.3    
# https://bittrex.com/api/v1.1/market/selllimit?apikey=API_KEY&market=BTC-LTC&quantity=1.2&rate=1.3    
# https://bittrex.com/api/v1.1/market/cancel?apikey=API_KEY&uuid=ORDER_UUID    
# https://bittrex.com/api/v1.1/market/getopenorders?apikey=API_KEY&market=BTC-LTC

# ACCOUNT API   
# https://bittrex.com/api/v1.1/account/getbalances?apikey=API_KEY    
# https://bittrex.com/api/v1.1/account/getbalance?apikey=API_KEY&currency=BTC    
# https://bittrex.com/api/v1.1/account/getdepositaddress?apikey=API_KEY&currency=VTC    
# https://bittrex.com/api/v1.1/account/withdraw?apikey=API_KEY&currency=EAC&quantity=20.40&address=EAC_ADDRESS    
# https://bittrex.com/api/v1.1/account/getorder&uuid=0cb4c4e4-bdc7-4e13-8c13-430e587d2cc1    
# https://bittrex.com/api/v1.1/account/getorderhistory    
# https://bittrex.com/api/v1.1/account/getwithdrawalhistory?currency=BTC    
# https://bittrex.com/api/v1.1/account/getdeposithistory?currency=BTC    
# 

public_cmds  = ["getmarkets", "getcurrencies", "getticker", "getmarketsummaries", \
                "getmarketsummary", "getorderbook", "getmarkethistory"]
market_cmds  = ["getmarkets", "buylimit", "selllimit", "cancel", "getopenorders"]

account_cmds = ["getbalances", "getbalance", "getdepositaddress", "withdraw", "getorder", \
                "getorderhistory", "getwithdrawalhistory", "getdeposithistory"]

class publicRex:

    def __init__(self, apiUrl):
        self.base_url = apiUrl
        self.public_urls = {}
    
        for cmd in public_cmds:
            self.public_urls[cmd] = self.base_url+cmd
            print self.public_urls[cmd]

    def process(self, json):
        status = json["success"]

        if status:
            print "Success!"
            response = json["result"]            
            return (True, response)
        else:
            print "Failed!"
            msg = json["message"]            
            return (False, msg)
	
    def getmarkets(self):
        req = requests.get(self.public_urls["getmarkets"])
        json = req.json() 
        return self.process(json)
        

    def getcurrencies(self):
        req = requests.get(self.public_urls["getcurrencies"])
        json = req.json()
        return self.process(json)

    def getticker(self, ticker1="", ticker2=""):
        if len(ticker1) == 0 or len(ticker2) == 0:
            print "getticker: pass a valid ticker pair"
            return

        ticker=ticker1+"-"+ticker2
        data= {"market": ticker}
        req = requests.get(url= self.public_urls["getticker"], data=data)
        json = req.json()
        return self.process(json)

    def getmarketsummaries(self):
        req = requests.get(self.public_urls["getmarketsummaries"])
        json = req.json()
        return self.process(json)

    def getmarketsummary(self, ticker1="", ticker2=""):
        if len(ticker1) == 0 or len(ticker2) == 0:
            print "getticker: pass a valid ticker pair"
            return

        ticker=ticker1+"-"+ticker2
        data= {"market": ticker}
        req = requests.get(self.public_urls["getticker"], data=data)
        json = req.json()
        return self.process(json)

    def getorderbook(self, ticker1="", ticker2="", ordertype="", depth=1):
        if len(ticker1) == 0 or len(ticker2) == 0:
            print "getticker: pass a valid ticker pair"
            return
        
        if len(ordertype) == 0:
            print "getOrderBook: Specify order type"
            return

        ticker=ticker1+"-"+ticker2
        data= {"market": ticker, "type": type, "depth": depth}
        req = requests.get(self.public_urls["getticker"], data=data)
        json = req.json()
        return self.process(json)
        
    def getmarkethistory(self, ticker1="", ticker2=""):
        if len(ticker1) == 0 or len(ticker2) == 0:
            print "getticker: pass a valid ticker pair"
            return

        ticker=ticker1+"-"+ticker2
        data= {"market": ticker}
        print data
        req = requests.get(self.public_urls["getticker"], data=data)
        json = req.json()
        return self.process(json)

p = publicRex(publicApiUrl)
ret, msg = p.getmarkets()
ret, msg = p.getcurrencies()
ret, msg = p.getticker("BTC", "LTC")
ret, msg = p.getmarketsummaries()
ret, msg = p.getmarketsummary("BTC", "LTC")
ret, msg = p.getorderbook("BTC", "LTC", "buy")
