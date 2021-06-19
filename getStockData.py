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

    def mostGainerStock(self):
        url = ('https://financialmodelingprep.com/api/v3/stock/gainers?apikey=%s' %
               (config.FMP_API))
        parsedData = (getStockList.getJsonparsedData(url))
        mostGainerData = parsedData['mostGainerStock']
        counter = 0
        topFiveList = []
        for i in mostGainerData:
            while counter != 5:  # Limit to only top 5
                topFiveList.append(str(counter+1) + '. ' + mostGainerData[counter]['ticker'] + ' $' + mostGainerData[counter]['price'] + ' ' +
                                   mostGainerData[counter]['changesPercentage'])    # Store ticker, price, and %change of stock
                counter += 1

        # print('\n'.join(topFiveList))
        return topFiveList
