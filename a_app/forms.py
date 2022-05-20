from dataclasses import fields
from django import forms
from .models import Profile


class Profile_form(forms.ModelForm):
     full_name=forms.CharField(widget=forms.TextInput(attrs=
        {"class":"form-control","placeholder":"Enter your Fullname"}))
     country=forms.CharField(widget=forms.TextInput(attrs=
        {"class":"form-control","placeholder":"Enter your Country"}))
     contact=forms.IntegerField(widget=forms.NumberInput(attrs=
        {"class":"form-control","placeholder":"Enter your Phone.no"}))
     profession=forms.CharField(widget=forms.TextInput(attrs=
        {"class":"form-control","placeholder":"Enter your profession"}))
                
     class Meta:
            model=Profile
            fields={'full_name','contact','country','profession','profile_pic'}
       