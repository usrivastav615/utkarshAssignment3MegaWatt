from django.conf.urls import url
from django.contrib import admin
from sites.views import *

urlpatterns = [
    url(r'^$', SitesList.as_view(), name='sitesList'),
    url(r'sites/(?P<pk>\d+)$', SitesDetailView.as_view(), name='siteDetail'),
    url(r'getSumOfSiteValues', SitesSum.as_view(), name='getSumOfSiteValues'),
    url(r'getAverageOfSiteValues', SitesAverage.as_view(), name='getAverageOfSiteValues'),
]