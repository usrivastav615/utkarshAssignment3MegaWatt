from base import *

class SitesSum(ListView):
    template_name = 'SiteSummary.html'

    def get(self, request, *args, **kwargs):
        return TemplateResponse(request, self.template_name,
                                self.get_context_data())

    def get_context_data(self):
        sites = Site.allSites.annotate(
            aggregateAValue=Sum('sitevalues__aValue'),
            aggregateBValue=Sum('sitevalues__bValue'),
        ).order_by('id')

        return {
            'sitesSummary': sites,
            'summary' : 'summation',
        }
