from rest_framework import serializers
from scrum_reports.models import ScrumReport


class ScrumReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrumReport
        fields = '__all__'
