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
            'company_name': forms.TextInput(attrs={'placeholder': 'Enter company name'}),
            'role_title': forms.TextInput(attrs={'placeholder': 'Enter job role'}),
            'job_link': forms.URLInput(attrs={'placeholder': 'Paste job URL'}),
            'status': forms.Select(),
            'date_applied': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'placeholder': 'Add notes', 'rows': 4}),
        }


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}),
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Choose a username'}),
        }
        help_texts = {
            'username': '',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].label = 'Username'
        self.fields['username'].widget.attrs.update({
            'class': 'form-input',
            'placeholder': 'Choose a username',
        })
        self.fields['username'].help_text = ''

        self.fields['email'].label = 'Email Address'
        self.fields['email'].widget.attrs.update({
            'class': 'form-input',
        })

        self.fields['password1'].label = 'Password'
        self.fields['password1'].widget.attrs.update({
            'class': 'form-input',
            'placeholder': 'Create a password',
        })
        self.fields['password1'].help_text = 'Use at least 8 characters with a mix of letters and numbers.'

        self.fields['password2'].label = 'Confirm Password'
        self.fields['password2'].widget.attrs.update({
            'class': 'form-input',
            'placeholder': 'Re-enter your password',
        })
        self.fields['password2'].help_text = 'Enter the same password again for confirmation.'