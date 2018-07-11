from base import *
from AllSitesManager import AllSitesManager

class Site(models.Model):
    name = models.CharField(max_length=100, default="", blank=True)
    slug = models.CharField(max_length=100, default="", blank=True)
    allSites = AllSitesManager()

    class Meta:
        db_table = 'sites_site'
