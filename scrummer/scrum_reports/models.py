from django.contrib.auth.models import User
from django.db import models


class SignUp(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.email


class ScrumReport(models.Model):
    person = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    report_since_last = models.TextField(blank=True)
    report_before_next = models.TextField(blank=True)
    report_issues = models.TextField(blank=True)

