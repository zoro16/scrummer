from django import forms
from scrum_reports.models import SignUp, ScrumReport


class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = '__all__'


class ScrumReportForm(forms.ModelForm):
    class Meta:
        model = ScrumReport
        fields = '__all__'
        widgets = {
            '__all__': forms.Textarea(attrs={'rows': 2}),
        }
