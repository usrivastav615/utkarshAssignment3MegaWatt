from base import *
from Site import *
from AllSiteValuesManager import *

class SiteValues(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    createdDate = models.DateTimeField(default=datetime.now, blank=False)
    aValue = models.FloatField(default = 0, blank=True)
    bValue = models.FloatField(default = 0, blank=True)
    allSiteValues = AllSiteValuesManager()

    class Meta:
        db_table = 'sites_sitevalues'