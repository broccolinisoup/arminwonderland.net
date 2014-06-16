# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BlogPost'
        db.create_table('home_blogpost', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('context', self.gf('tinymce.models.HTMLField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('home', ['BlogPost'])


    def backwards(self, orm):
        # Deleting model 'BlogPost'
        db.delete_table('home_blogpost')


    models = {
        'home.blogpost': {
            'Meta': {'object_name': 'BlogPost', 'ordering': "['date']"},
            'context': ('tinymce.models.HTMLField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        }
    }

    complete_apps = ['home']