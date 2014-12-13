from django import forms
from django.forms import ModelForm
from arminwonderland.home.models import Contacts
from django.forms.extras import widgets

class DifferentlySizedTextarea(forms.Textarea):
  def __init__(self, *args, **kwargs):
    attrs = kwargs.setdefault('attrs', {})
    attrs.setdefault('cols', 80)
    attrs.setdefault('rows', 5)
    super(DifferentlySizedTextarea, self).__init__(*args, **kwargs)



class ContactForm(forms.ModelForm):

    name = forms.CharField(label='Name', required=True, error_messages={'required': 'Please enter your name'}, max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Name', 'id':'name'}))
    email= forms.EmailField(label='Email Address', required=True, error_messages={'required': 'Please enter your email address'}, max_length=100, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address', 'id':'email'}))
    content= forms.CharField(label='Message', required=True,error_messages={'required': 'Please enter your message'}, max_length=500, widget=DifferentlySizedTextarea(attrs={'class':'form-control','placeholder':'Message', 'id':'message'}))

    class Meta:
    	model = Contacts
    	fields = ['name', 'email', 'content']