from django import forms

from .models import JobApplication


class JobForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = [
            'company_name',
            'role_title',
            'job_link',
            'status',
            'date_applied',
            'notes',
        ]
        widgets = {
            'date_applied': forms.DateInput(attrs={'type': 'date'}),
        }
