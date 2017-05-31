from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import RedirectView

import debug_toolbar

urlpatterns = [
    url(r'^scrum-reports/', include('scrum_reports.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^__debug__/', include(debug_toolbar.urls)),
    url(r'^$',
        RedirectView.as_view(url='/scrum-reports/home/', permanent=False)
    )
]
