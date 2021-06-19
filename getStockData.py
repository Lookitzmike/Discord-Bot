import config

try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

import json


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
        counter = 0
        topFiveList = []
        for i in mostGainerData:
            while counter != 5:  # Limit to only top 5
                topFiveList.append(str(counter+1) + '. ' + mostGainerData[counter]['ticker'] + ' $' + mostGainerData[counter]['price'] + ' ' +
                                   mostGainerData[counter]['changesPercentage'])    # Store ticker, price, and %change of stock
                counter += 1
        return topFiveList

    def getGainerTicker():  # Process data select only ticker for graph
        parsedStockData = getStockList.getMostGainerStock()
        mostGainerData = parsedStockData['mostGainerStock']
        counter = 0
        tickerList = []
        for i in mostGainerData:
            while counter != 5:  # Limit to only top 5
                tickerList.append(mostGainerData[counter]['ticker'])
                counter += 1
        return tickerList

    # Get historic data of each ticker from top 5 gainer stocks
    def historicStockData(self):
        tickerList = getStockList.getGainerTicker()
        # topFiveTickerList = []
        # for i in tickerList:
        #     url = ("https://financialmodelingprep.com/api/v3/historical-price-full/%s?apikey=%s" %
        #            (tickerList, config.FMP_API_HISTORIC_DATA))
        #     parsedHistoricalData = (getStockList.getJsonparsedData(url))
        #     topFiveTickerList.append(parsedHistoricalData['symbol'])
        return tickerList
