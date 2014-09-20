from django import forms
from django.forms import ModelForm
from aydoganersoz.home.models import Contacts

class ContactForm(ModelForm):
    class Meta:
    	model = Contacts
    	fields = ['name', 'email', 'content']