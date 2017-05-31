from django.views.generic import ListView, CreateView, DetailView
from scrum_reports.models import ScrumReport
from scrum_reports.forms import ScrumReportForm
from django.urls import reverse_lazy
from rest_framework import generics
from scrum_reports.serializers import ScrumReportSerializer


class ScrumReportList(generics.ListCreateAPIView):
    """
    API endpoint for listing and creating Book objects
    """
    queryset = ScrumReport.objects.all()
    serializer_class = ScrumReportSerializer


class HomeView(CreateView):
    template_name = 'scrum_reports/home.html'
    model = ScrumReport
    form_class = ScrumReportForm
    success_url = reverse_lazy('home')

    def scrumreports(self):
        return ScrumReport.objects.order_by('-created')[:3]


class ReportView(ListView):
    template_name = 'scrum_reports/reports.html'
    queryset = ScrumReport.objects.order_by('-created')
    paginate_by = 10


class ReportDetailView(DetailView):
    model = ScrumReport
    success_url = reverse_lazy('report-detail')
