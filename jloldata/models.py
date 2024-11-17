# models.py

from django.db import models

class JlolData(models.Model):
    dt_ct_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    joining = models.CharField(max_length=100)
    ol_date = models.DateField(null=True, blank=True)  # Add this field for OL date

    def __str__(self):
        return self.username
