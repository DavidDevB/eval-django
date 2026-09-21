from django import forms
from .models import Demande

class DemandeForm(forms.ModelForm):
    class Meta:
        model = Demande
        fields = ['activite', 'competence', 'creneau']
        widgets = {
            'creneau': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }