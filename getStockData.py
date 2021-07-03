import config

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

import json

amountOfStockOutput = 5
count = 0


class getStockList:

    def getJsonparsedData(url):
        """
        https://financialmodelingprep.com/developer/docs/most-gainers-stock-market-data-free-api/
        Receive the content of "url", parse it as JSON and return the object.

        Parameters
        ----------
        url : str

        Returns
        -------
        dict
        """
        response = urlopen(url)
        data = response.read().decode('utf-8')
        return json.loads(data)

    def getMostGainerStock():   # Get data from FMP api
        url = ('https://financialmodelingprep.com/api/v3/stock/gainers?apikey=%s' %
               (config.FMP_API_STOCK_LIST))
        parsedStockData = (getStockList.getJsonparsedData(url))
        return parsedStockData

    # Process data select only ticker, price, and % change
    def printGainerStock(self):
        parsedStockData = getStockList.getMostGainerStock()
        mostGainerData = parsedStockData['mostGainerStock']
        topFiveList = []
        global count
        for i in mostGainerData:
            while count != amountOfStockOutput:  # Limit amount of stock outputs
                topFiveList.append(str(count+1) + '. ' + mostGainerData[count]['ticker'] + ' $' + mostGainerData[count]['price'] + ' ' +
                                   mostGainerData[count]['changesPercentage'])    # Store ticker, price, and %change of stock
                count += 1
        return topFiveList

    def getGainerTicker():  # Process data select only ticker for graph
        parsedStockData = getStockList.getMostGainerStock()
        mostGainerData = parsedStockData['mostGainerStock']
        tickerList = []
        global count
        for i in mostGainerData:
            while count != amountOfStockOutput:
                tickerList.append(mostGainerData[count]['ticker'])
                count += 1
        return tickerList

    # Get historic data of each ticker from top gainer stocks
    def historicStockData(self):
        url_P1 = ("https://financialmodelingprep.com/api/v3/historical-price-full/")
        url_P2 = ("?apikey=%s" % (config.FMP_API_HISTORIC_DATA))
        tickerList = getStockList.getGainerTicker()
        topFiveTickerList = []
        count = 0
        for i in range(len(tickerList)):
            while count != len(tickerList):
                url = url_P1+tickerList[count]+url_P2
                parsedHistoricalData = (getStockList.getJsonparsedData(url))
                topFiveTickerList.append(parsedHistoricalData['symbol'] + " " + parsedHistoricalData['historical'][0]['date'] + " Close price: " + str(
                    parsedHistoricalData['historical'][0]['close']))    # *Reminder: Store in hash table linked list instead
                count += 1
        return topFiveTickerList
