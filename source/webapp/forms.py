from django import forms
from django.forms import widgets

from webapp.models import STATUS_CHOICES

class TaskForm(forms.Form):
    status = forms.ChoiceField(widget=forms.RadioSelect, choices=STATUS_CHOICES)
    title = forms.CharField(max_length=50, required=True, label='Title')
    description = forms.CharField(max_length=3000, required=True, label='Description', widget=widgets.Textarea(attrs={'cols': 20, 'rows': 3}))
    to_do_date = forms.CharField(max_length=50, required=False, label='To do date')
