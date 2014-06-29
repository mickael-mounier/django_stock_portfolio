from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from functools import wraps

from models import Stock, Portfolio

from datetime import date, timedelta
import urllib2
import urllib
import json

def execute_yql_query_(query):
    url = 'http://query.yahooapis.com/v1/public/yql?q='
    url += urllib.quote_plus(query)
    url += '&format=json&env=store://datatables.org/alltableswithkeys'
    res = json.loads(urllib2.urlopen(url).read())
    import pprint ; pprint.pprint(res)
    return res

def yahoo_get_symbol(symbol):
    return execute_yql_query_('select * from yahoo.finance.quote where symbol = "' + symbol + '"')

def yahoo_get_hist(symbol, start=None, end=None):
    if start is None and end is None:
        end = date.today() - timedelta(days=1)
        start = end - timedelta(days=366)
    return execute_yql_query_('select * from yahoo.finance.historicaldata where symbol = "' + symbol +
                              '" and startDate = "' + start.strftime('%Y-%m-%d') +
                              '" and endDate = "' + end.strftime('%Y-%m-%d') +'"')


def get_portfolio_from_id(fatal=False):
    def wrap(func):
        @wraps(func)
        def f_get_portfolio_from_id(*args, **kwargs):
            try:
                kwargs['portfolio'] = Portfolio.objects.get(pk=kwargs['portfolio_id'])
            except ObjectDoesNotExist:
                if fatal:
                    raise Http404
                kwargs['portfolio'] = None
            return func(*args, **kwargs)
        return f_get_portfolio_from_id
    return wrap

def get_stock_from_symbol(fatal=False):
    def wrap(func):
        @wraps(func)
        def f_get_stock_from_symbol(*args, **kwargs):
            try:
                kwargs['stock'] = Stock.objects.get(pk=kwargs['symbol'])
            except ObjectDoesNotExist:
                if fatal:
                    raise Http404
                kwargs['stock'] = None
            return func(*args, **kwargs)
        return f_get_stock_from_symbol
    return wrap
