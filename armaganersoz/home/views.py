#! /usr/bin/env python2.7
from django.views.generic import TemplateView
from armaganersoz.home.models import BlogPost
from armaganersoz.home.forms import ContactForm
from django.template.response import TemplateResponse

class HomeView(TemplateView):
	template_name = 'home.html'

	def get(self, request, *args, **kwargs):

		blog_posts = BlogPost.objects.all()
		form = ContactForm()
		context = {
			'blog_posts': blog_posts,
			'form': form,
		}
		return self.render_to_response(context)

	def post(self, request, *args, **kwargs):

		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
		return render_to_response({'form':form})



class BlogView(TemplateView):
	template_name = 'blog_detail.html'

	def get(self, request, *args, **kwargs):

		id=self.kwargs['id']

		blog_post = BlogPost.objects.get(id=1)

		context = {
			'blog_post': blog_post,
		}

		return self.render_to_response(context)