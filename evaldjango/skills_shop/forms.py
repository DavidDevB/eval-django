from django import forms
from .models import Query

class QueryForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = ['activity', 'skill', 'slot']
        widgets = {
            'slot': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }