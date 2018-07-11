from base import *

class AllSitesManager(models.Manager):
    def get_queryset(self):
        return super(AllSitesManager, self).get_queryset().all()