from django import forms
from django.forms import ModelForm
from arminwonderland.home.models import Contacts

class ContactForm(ModelForm):
    class Meta:
    	model = Contacts
    	fields = ['name', 'email', 'content']