from django.contrib import admin
from armaganersoz.home.models import BlogPost, Contacts
class BlogPostAdmin(admin.ModelAdmin):
    pass

class ContactsAdmin(admin.ModelAdmin):
    pass
admin.site.register(BlogPost, BlogPostAdmin)    
admin.site.register(Contacts, ContactsAdmin)
