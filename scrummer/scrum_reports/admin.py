from django.contrib import admin
from scrum_reports.models import SignUp, ScrumReport


@admin.register(ScrumReport)
class ScrumReportAdmin(admin.ModelAdmin):
    list_display = ('person', 'created')


@admin.register(SignUp)
class SignUpAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'timestamp')

