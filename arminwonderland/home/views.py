#! /usr/bin/env python2.7
from django.views.generic import ListView, TemplateView, DetailView, FormView, CreateView
from django.views.generic.base import TemplateResponseMixin
from datetime import datetime
from arminwonderland.home.models import TechnicalWriting, Contacts
from arminwonderland.home.forms import ContactForm
from django.template.response import TemplateResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
import tweepy


class HomeView(ListView):
    template_name = 'home.html'
    # context_object_name is 'object_list' as a default name.
    # If you want to change, overwrite context_object_name

    def get_queryset(self):
        return TechnicalWriting.objects.order_by('-publish_date')

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        auth = tweepy.OAuthHandler('c5gkYaphnz2FHBqDHPlYR8jL0', 'czgaosLx924cbNMHwBxGuu7bhI1NklQUPIBG2DHzktR2SSagWx')
        auth.set_access_token('572070033-PKjreF1SGh6Zdggj7YAa3jMmIqQfC161bEVLj5tQ', '9nWH4JOqXZfiVbjNpTPnm87p5kj51olQWayzwKl7bU4Kn')
        api = tweepy.API(auth)
        my_tweets = api.user_timeline()
        context['twitter'] = my_tweets
        context['writings'] = TechnicalWriting.objects.order_by('-publish_date')
        return context


class TweeterView(ListView):
    template_name = 'stream.html'

    def get_queryset(self):
        auth = tweepy.OAuthHandler('c5gkYaphnz2FHBqDHPlYR8jL0', 'czgaosLx924cbNMHwBxGuu7bhI1NklQUPIBG2DHzktR2SSagWx')
        auth.set_access_token('572070033-PKjreF1SGh6Zdggj7YAa3jMmIqQfC161bEVLj5tQ', '9nWH4JOqXZfiVbjNpTPnm87p5kj51olQWayzwKl7bU4Kn')
        api = tweepy.API(auth)
        public_tweets = api.user_timeline()
        return public_tweets


class BlogView(DetailView):
    model = TechnicalWriting
    # context_object_name is 'object' as a default name.
    # If you want to change, overwrite context_object_name
    template_name = 'technical_writings_detail.html'


class AboutView(TemplateView):
    template_name = 'about_me.html'

'''
class ContactView(TemplateView):
    template_name = 'contact.html'
    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {'form':form,}
        return self.render_to_response(context,)
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        success=False
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']
            obj = form.save(commit=False)
            obj.date =datetime.now()
            obj.save()
            success = True
            form = ContactForm()
        context = {'form' : form,'success':success,}
        return self.render_to_response(context)
'''


class ContactView(CreateView):
    template_name = 'contact.html'
    model = Contacts
    fields = ['name', 'email', 'content']

