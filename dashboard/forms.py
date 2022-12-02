from django import forms
from . models import *
from django.forms import widgets

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'description']
        

class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        widgets = {'due': widgets.DateInput(attrs={"type":"date"})}
        fields = ['subject', 'title', 'description', 'due', 'is_finished']
        
class DashboardForm(forms.Form):
    text = forms.CharField(max_length=100, label="Enter Your Search")
    
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'is_finished']