from base import *

class SitesDetailView(DetailView):
    model = Site
    template_name = 'SiteDetails.html'

    def get(self, request, *args, **kwargs):
        return TemplateResponse(request, self.template_name,
                                self.get_context_data())

    def get_context_data(self):
        site = self.get_object()
        return {
            "name" : site.name,
            "siteValues" : site.sitevalues_set.all()
        }

    def get_object(self):
        return get_object_or_404(Site, pk=self.kwargs.get("pk"))
