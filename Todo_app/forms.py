from django import forms
from django.forms import ModelForm
from . models import *


class task_form(forms.ModelForm):
    
    class Meta:
        model = Task
        fields = {'title','completed','consumed_hours','due_time'}
