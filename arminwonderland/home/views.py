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
		blog_posts = BlogPost.objects.order_by('date')
		context = {'form':form,'blog_posts': blog_posts}
		return self.render_to_response(context,)
	def post(self, request, *args, **kwargs):
		form = ContactForm(request.POST)
		success=False
		blog_posts=[]


		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			content = form.cleaned_data['content']
			obj = form.save(commit=False)
			obj.date =datetime.now()
			obj.save()
			success = True
			form = ContactForm()
			blog_posts = BlogPost.objects.order_by('date')

		context = {
			'form' : form,
			'success':success,
			'blog_posts':blog_posts,

		}
		return self.render_to_response(context)

class BlogView(TemplateView):
	template_name = 'technical_writings_detail.html'

	def get(self, request, *args, **kwargs):
		id = self.kwargs['id']
		blog_post = BlogPost.objects.get(id=id)

		context = {'blog_post':blog_post }
		return self.render_to_response(context,)
