from django import forms
from .models import RecordListDB

class RecordForm(forms.ModelForm):
    
    class Meta:
        model = RecordListDB
        fields = ("person", "record_datetime", "image")
