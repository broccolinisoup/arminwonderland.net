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
		blog_posts = BlogPost.objects.order_by('-date')
		context = {'blog_posts': blog_posts}
		return self.render_to_response(context,)


class BlogView(TemplateView):
	template_name = 'technical_writings_detail.html'

	def get(self, request, *args, **kwargs):
		id = self.kwargs['id']
		blog_post = BlogPost.objects.get(id=id)

		context = {'blog_post':blog_post }
		return self.render_to_response(context,)

class AboutView(TemplateView):
	template_name = 'about_me.html'

	def get(self, request, *args, **kwargs):
		context = {}
		return self.render_to_response(context,)

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


		context = {
			'form' : form,
			'success':success,


		}
		return self.render_to_response(context)
