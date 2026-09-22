from django import forms
from .models import Demande

class DemandeForm(forms.ModelForm):
    class Meta:
        model = Demande
        fields = ['activity', 'skill', 'slot']
        widgets = {
            'slot': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }