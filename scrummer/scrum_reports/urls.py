from django.conf.urls import url
from scrum_reports.views import ReportView, HomeView, ReportDetailView, ScrumReportList


urlpatterns = [
    url(r'home/$', HomeView.as_view(), name='home'),
    url(r'reports/$', ReportView.as_view(), name='reports'),
    url(r'^report/(?P<pk>\d+)$', ReportDetailView.as_view(), name='report-detail'),
    url(r'list/$', ScrumReportList.as_view(), name='scrum-reports-list'),
]
