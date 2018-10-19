from django.urls import include, path
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

from oscar.app import application
from paypal.payflow.dashboard.app import application as payflow
from paypal.express.dashboard.app import application as express_dashboard

admin.autodiscover()

urlpatterns = [

    path('i18n/', include('django.conf.urls.i18n')),
# PayPal Express integration...
    path('checkout/paypal/', include('paypal.express.urls')),
    # Dashboard views for Payflow Pro
    path('dashboard/paypal/payflow/', payflow.urls),
    # Dashboard views for Express
    path('dashboard/paypal/express/', express_dashboard.urls),
    # url(r'', application.urls),
]
# urlpatterns += i18n_patterns(
#
# )

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns