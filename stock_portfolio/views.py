from django.shortcuts import render, redirect

from models import Stock, Portfolio
from helpers import get_portfolio_from_id, get_stock_from_symbol

def home(request):
    return render(request, 'stock_portfolio/home.html', {})

@get_portfolio_from_id(fatal=True)
def portfolio(request, portfolio_id, portfolio):
        return render(request, 'stock_portfolio/portfolio.html', {})

# FIXME: move this somewhere else
def new_stock(symbol):
    stock = Stock(symbol=symbol)
    stock.save()
    return stock

@get_portfolio_from_id(fatal=True)
@get_stock_from_symbol
def portfolio_add_stock(request, portfolio_id, portfolio, symbol, stock):
    if stock is None:
        sotck = new_stock(symbol)
        pass # FIXME: create it!
    return redirect('portfolio', {'portfolio_id': portfolio_id})

# TO READ: http://stackoverflow.com/questions/17245498/get-stock-quotes-from-yahoo-finance-in-json-format-using-a-javascript
