from django.contrib import admin
from arminwonderland.home.models import BlogPost, Contacts
from django.forms import TextInput, Textarea
from django.db import models
from tinymce.widgets import TinyMCE

class BlogPostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        #models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': TinyMCE(attrs={'rows':20, 'cols':150})},
    }

class ContactsAdmin(admin.ModelAdmin):
    pass


admin.site.register(BlogPost, BlogPostAdmin)    
admin.site.register(Contacts, ContactsAdmin)


