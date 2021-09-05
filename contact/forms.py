from django import forms
from django.contrib.auth.models import User
from .models import Contact



class ContactForm(forms.Form):
    
    name = forms.CharField()
    email = forms.EmailField()
    number = forms.IntegerField()
    message = forms.CharField(widget=forms.Textarea)



class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'number', 'message']    

