from django.contrib import admin
from arminwonderland.home.models import BlogPost, Contacts
from django.forms import TextInput, Textarea
from django.db import models

class BlogPostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        #models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }

class ContactsAdmin(admin.ModelAdmin):
    pass


admin.site.register(BlogPost, BlogPostAdmin)    
admin.site.register(Contacts, ContactsAdmin)


