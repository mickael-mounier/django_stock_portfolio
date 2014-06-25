from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from functools import wraps

from models import Stock, Portfolio

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
