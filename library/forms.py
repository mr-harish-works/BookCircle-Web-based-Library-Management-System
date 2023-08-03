from django import forms
from django.contrib.auth.models import User
from . import models

class IssueBookForm(forms.Form):
    isbn2 = forms.ModelChoiceField(queryset=models.Book.objects.all(), empty_label="Book Name ", to_field_name="isbn", label="Book Details")
    name2 = forms.ModelChoiceField(queryset=models.Student.objects.all(), empty_label="Student Details", to_field_name="user", label="Student Details")
    
    isbn2.widget.attrs.update({'class':'form-control'})
    name2.widget.attrs.update({'class':'form-control'})
