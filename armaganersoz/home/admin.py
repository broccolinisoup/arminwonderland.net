from django.contrib import admin
from armaganersoz.home.models import BlogPost
class BlogPostAdmin(admin.ModelAdmin):
    pass
admin.site.register(BlogPost, BlogPostAdmin)
