#!/usr/bin/env python
import config
import os
import sys
import cProfile
import pstats


try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

import json
from time import perf_counter

count = 0


def getJsonparsedData(url):
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)


def getRealTimeStock():
    url_P1 = ("https://financialmodelingprep.com/api/v3/quote-short/")
    url_P2 = ("?apikey=%s" % (config.FMP_API))
    stockList = ['GME', 'AMC']
    dataList = []
    global count
    for i in range(len(stockList)):
        while count != len(stockList):
            url = url_P1+stockList[count]+url_P2
            realTimeData = (getJsonparsedData(url))
            dataList.append(realTimeData)
            count += 1
    return dataList


def main():
    # Test for how long each function takes to run
    with cProfile.Profile() as pr:
        getRealTimeStock()
    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    # stats.print_stats()
    stats.dump_stats(filename='profiling.prof')
    # in bash: snakeviz ./profiling.prof


# getRealTimeStock()
if __name__ == '__main__':
    main()
