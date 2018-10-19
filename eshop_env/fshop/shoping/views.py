from django.shortcuts import render

# Create your views here.
from oscar.apps.promotions.views import HomeView as CoreHomeView


class HomeView(CoreHomeView):
    template_name = 'promotions/new-homeview.html'

from django.utils.translation import ugettext_lazy as _




from paypal.express.views import RedirectView as OscarPaypalRedirectView


class RedirectView(OscarPaypalRedirectView):
    def _get_paypal_params(self):
        return {
            'SOLUTIONTYPE': 'Mark',
            'LANDINGPAGE': 'Login',
            'BRANDNAME': 'My Brand name'
        }