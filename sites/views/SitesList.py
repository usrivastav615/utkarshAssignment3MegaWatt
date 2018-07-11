from base import *

class SitesList(ListView):
    template_name = 'SitesList.html'
    context_object_name = "sites_list"

    def get_queryset(self):
        try:
            sites = Site.allSites.all()
        except Site.DoesNotExist:
            sites = None
        return sites