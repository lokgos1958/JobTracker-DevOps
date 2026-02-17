from django import forms
from .models import JobApplication

class JobForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        # We list only the fields we want the user to fill in.
        # We EXCLUDE 'user' because we will fill that in automatically in the view.
        fields = ['company_name', 'role_title', 'job_link', 'status', 'date_applied', 'notes']
        
        # This adds a calendar widget to the date field so you don't have to type it manually.
        widgets = {
            'date_applied': forms.DateInput(attrs={'type': 'date'}),
        }