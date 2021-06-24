import config
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

import json
import os
import sys


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
    parsedStockData = (getJsonparsedData(url))
    return parsedStockData


def getGainerTicker():  # Process data select only ticker for graph
    parsedStockData = getMostGainerStock()
    mostGainerData = parsedStockData['mostGainerStock']
    counter = 0
    tickerList = []
    for i in mostGainerData:
        while counter != 5:  # Limit to only top 5
            tickerList.append(mostGainerData[counter]['ticker'])
            counter += 1
    return tickerList


def historicStockData():
    url_P1 = ("https://financialmodelingprep.com/api/v3/historical-price-full/")
    url_P2 = ("?apikey=%s" % (config.FMP_API_HISTORIC_DATA))
    topFiveTickerList = ['ENTX', 'BEST']
    dateList = []
    for i in range(len(topFiveTickerList)):
        url = url_P1+topFiveTickerList[i]+url_P2
        print(url)
        parsedHistoricalData = getJsonparsedData(url)
        dateList.append(parsedHistoricalData['historical'][0]['date'] + " Open price: " + str(
            parsedHistoricalData['historical'][0]['open']))
        # dateData = parsedHistoricalData['historical'][0]['date']
        # openData = str(parsedHistoricalData['historical'][0]['open'])
        # dateList.append(dateData)
        # dateList.append(openData)
        return dateList
    #     sys.stdout = open("test.json", "w")
    #     print(getJsonparsedData(url))
    # sys.stdout.close()


print(historicStockData())
