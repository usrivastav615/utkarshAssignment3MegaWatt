from base import *

class AllSiteValuesManager(models.Manager):
    def get_queryset(self):
        return super(AllSiteValuesManager, self).get_queryset().all()