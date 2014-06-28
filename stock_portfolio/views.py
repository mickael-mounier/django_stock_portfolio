from django.shortcuts import render, redirect
from django.http import HttpResponse

from models import Stock, Portfolio
from helpers import get_portfolio_from_id, get_stock_from_symbol, yahoo_get_hist

import json

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
    return render(request, 'stock_portfolio/stock.html', {'stock': stock,
                                                          'hist': json.dumps(hist)})
