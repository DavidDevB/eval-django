from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Query, Skill

class QueryForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = ['activity', 'skill', 'slot']
        widgets = {
            'slot': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class SignupForm(UserCreationForm):
    skills = forms.ModelMultipleChoiceField(
        queryset=Skill.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta(UserCreationForm.Meta):
        fields = (*UserCreationForm.Meta.fields, 'skills')