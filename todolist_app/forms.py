from django import forms
from django.forms import ModelForm

#import django_tables2 as tables

from .models import *

class TaskForm(forms.ModelForm):
    title = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...'}))
    class Meta: #minimal 2 values
        model = Task #model for what (Task)
        fields = '__all__'
