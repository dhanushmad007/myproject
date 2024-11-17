# forms.py

from django import forms
from .models import JlolData

class OLDateForm(forms.ModelForm):
    class Meta:
        model = JlolData
        fields = ['ol_date']
        widgets = {
            'ol_date': forms.DateInput(attrs={'type': 'date'}),
        }
