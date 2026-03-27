from django.contrib.auth.models import User
from django.db import models


class JobApplication(models.Model):
    STATUS_CHOICES = [
        ('APPLIED', 'Applied'),
        ('INTERVIEW', 'Interview Scheduled'),
        ('OFFER', 'Offer Received'),
        ('REJECTED', 'Rejected'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    company_name = models.CharField(max_length=100)
    role_title = models.CharField(max_length=100)
    job_link = models.URLField(max_length=200)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='APPLIED',
    )
    date_applied = models.DateField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.company_name} - {self.role_title}"
