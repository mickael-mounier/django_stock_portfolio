from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Home
    url(r'^$', 'stock_portfolio.views.home', name='home'),

    # Portfolios
    url(r'^portfolio/(?P<portfolio_id>[1-9][0-9]*)/$', 'stock_portfolio.views.portfolio', name='portfolio'),
    url(r'^portfolio/(?P<portfolio_id>[1-9][0-9]*)/add/(?P<symbol>[^/]+)/$', 'stock_portfolio.views.portfolio_add_stock', name='portfolio_add_stock'),

    # Admin
    url(r'^admin/', include(admin.site.urls)),
)
