#! /usr/bin/env python2.7
from django.views.generic import TemplateView
from datetime import datetime
from aydoganersoz.home.models import BlogPost
from aydoganersoz.home.forms import ContactForm
from django.template.response import TemplateResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

class HomeView(TemplateView):
	template_name = 'home.html'

	def get(self, request, *args, **kwargs):
		context = {}
		return self.render_to_response(context,)

class BlogPostView(TemplateView):
	template_name = 'blog_post.html'

	def get(self, request, *args, **kwargs):


		blog_posts = BlogPost.objects.all()

		context = {
			'blog_posts': blog_posts,
		}

		return self.render_to_response(context)

class AboutMeView(TemplateView):
	template_name = 'aboutme.html'

	def get(self, request, *args, **kwargs):

		context = {}
		return self.render_to_response(context)


class ContactView(TemplateView):
	template_name = 'contact.html'

	def get(self, request, *args, **kwargs):
		form = ContactForm()
		context = {'form': form,}
		return self.render_to_response(context)

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


