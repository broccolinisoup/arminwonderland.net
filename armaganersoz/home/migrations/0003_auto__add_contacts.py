# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contacts'
        db.create_table('home_contacts', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=32)),
            ('content', self.gf('django.db.models.fields.TextField')(max_length=1024, blank=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('home', ['Contacts'])


    def backwards(self, orm):
        # Deleting model 'Contacts'
        db.delete_table('home_contacts')


    models = {
        'home.blogpost': {
            'Meta': {'ordering': "['date']", 'object_name': 'BlogPost'},
            'context': ('tinymce.models.HTMLField', [], {}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        'home.contacts': {
            'Meta': {'ordering': "['date']", 'object_name': 'Contacts'},
            'content': ('django.db.models.fields.TextField', [], {'max_length': '1024', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '32'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['home']