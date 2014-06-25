from django.db import models

class Stock(models.Model):
    yahoo_symbol = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=100)
    market = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    stocks = models.ManyToManyField('Stock')
    def __str__(self):
        return self.name

class Order(models.Model):
    SIDES = (
        ('B', 'Buy'),
        ('S', 'Sell'),
    )
    side = models.CharField(max_length=1, choices=SIDES)
    stock = models.ForeignKey('Stock')
    portfolio = models.ForeignKey('Portfolio')
    qty = models.IntegerField()
    exec_time = models.DateTimeField()
    price = models.FloatField()
    fee = models.FloatField()
    def __str__(self):
        return '%s |  %s %s%s@%s' % (self.exec_time, self.stock.yahoo_symbol, '+' if self.side == 'B' else '-', self.qty, self.price)
