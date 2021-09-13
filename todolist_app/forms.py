from django import forms
from django.forms import ModelForm

from .models import *

class TaskForm(forms.ModelForm):
    class Meta: #minimal 2 values
        model = Task #model for what (Task)
        fields = '__all__'
