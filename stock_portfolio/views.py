from django.shortcuts import render, redirect
from django.http import HttpResponse

from models import Stock, Portfolio
from helpers import get_portfolio_from_id, get_stock_from_symbol, yahoo_get_hist

import json
import time

def home(request):
    return render(request, 'stock_portfolio/home.html', {'portfolios': Portfolio.objects.all()})

@get_portfolio_from_id(fatal=True)
def portfolio(request, portfolio_id, portfolio):
    return render(request, 'stock_portfolio/portfolio.html', {'portfolio': portfolio})

@get_portfolio_from_id(fatal=True)
@get_stock_from_symbol()
def portfolio_add_stock(request, portfolio_id, portfolio, symbol, stock):
    if stock is None:
        stock = Stock(yahoo_symbol=symbol)
        stock.save()
    portfolio.stocks.add(stock)
    portfolio.save()
    return HttpResponse('')

@get_stock_from_symbol(fatal=True)
def stock(request, symbol, stock):
    hist = yahoo_get_hist(symbol)['query']['results']['quote']
    stock_data = [[int(time.mktime(time.strptime(d['Date'], '%Y-%m-%d')) * 1000),
                   float(d['Adj_Close'])] for d in hist]
    stock_data.sort(key=lambda x: x[0])
    import pprint ; pprint.pprint(hist)
    return render(request, 'stock_portfolio/stock.html', {'stock': stock,
                                                          'stock_data': json.dumps(stock_data)})
