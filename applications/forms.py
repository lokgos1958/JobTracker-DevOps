from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']