from django.db.models.signals import pre_save
from helpers import yahoo_get_symbol
from django.dispatch import receiver
from models import Stock

@receiver(pre_save, sender=Stock)
def stock_pre_save(instance, *args, **kwargs):
    d = yahoo_get_symbol(instance.yahoo_symbol)
    print d
    if d['query']['count'] != 1:
        return
    d = d['query']['results']['quote']
    if instance.name is None or not instance.name:
        instance.name = d['Name']
    if instance.market is None or not instance.market:
        instance.market = d['StockExchange']
