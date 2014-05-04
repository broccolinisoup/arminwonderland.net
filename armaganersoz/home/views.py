#! /usr/bin/env python2.7
from django.views.generic import TemplateView
from models import BlogPost
from django.template.response import TemplateResponse

class HomeView(TemplateView):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):

    	blog_posts = BlogPost.objects.all()
        context = {
            'blog_posts': blog_posts,
        }
        return self.render_to_response(context)

class BlogView(TemplateView):
	template_name = 'blog_detail.html'

	def get(self, request, *args, **kwargs):

		print self.kwargs['id']

		blog_post = BlogPost.objects.get(id=1)

		context = {
            'blog_post': blog_post,
        }

		return self.render_to_response(context)

class AboutMeView(TemplateView):
    template_name = 'aboutme.html'

    def get(self, request, *args, **kwargs):

        return TemplateResponse(request, 'aboutme.html', {})