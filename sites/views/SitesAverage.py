from base import *

class SitesAverage(ListView):
    template_name = 'SiteSummary.html'

    def get(self, request, *args, **kwargs):
        return TemplateResponse(request, self.template_name,
                                self.get_context_data())

    def get_context_data(self):

        sqlQuery = 'select sites_site.id, name, avg("aValue") as "aggregateAValue", avg("bValue") as "aggregateBValue" from sites_site left outer join sites_sitevalues on sites_site.id = sites_sitevalues.site_id group by sites_site.id order by sites_site.id;'
        sites = []
        try:
            sites = Site.allSites.raw(sqlQuery)
        except Exception as e:
            pass

        return {
            'sitesSummary': sites,
            'summary': 'average',
        }

