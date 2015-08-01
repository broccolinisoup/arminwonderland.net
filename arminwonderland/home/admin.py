from django.contrib import admin
from arminwonderland.home.models import TechnicalWriting, Contacts
from django.forms import TextInput, Textarea
from django.db import models
from tinymce.widgets import TinyMCE
from ckeditor.widgets import CKEditorWidget


class TechnicalWritingAdmin(admin.ModelAdmin):
    formfield_overrides = {
        # models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': CKEditorWidget()},
    }


class ContactsAdmin(admin.ModelAdmin):
    pass


admin.site.register(TechnicalWriting, TechnicalWritingAdmin)
admin.site.register(Contacts, ContactsAdmin)


