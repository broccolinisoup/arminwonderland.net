#! /usr/bin/env python2.7
from django.views.generic import TemplateView
from datetime import datetime
from arminwonderland.home.models import BlogPost
from arminwonderland.home.forms import ContactForm
from django.template.response import TemplateResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

class HomeView(TemplateView):
	template_name = 'home.html'

	def get(self, request, *args, **kwargs):
		form = ContactForm()
		blog_posts = BlogPost.objects.all()
		context = {'form':form,'blog_posts': blog_posts}
		return self.render_to_response(context,)
	def post(self, request, *args, **kwargs):
		form = ContactForm(request.POST)
		success = False

		if form.is_valid():
			obj = form.save(commit=False)
			obj.date =datetime.now()
			obj.save()
			success = True
		context = {
			'form' : form,
			'success':success,

		}
		return self.render_to_response(context)

