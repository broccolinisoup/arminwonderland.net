# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BlogPost'
        db.create_table(u'home_blogpost', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('context', self.gf('django.db.models.fields.CharField')(max_length=323232)),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'home', ['BlogPost'])


    def backwards(self, orm):
        # Deleting model 'BlogPost'
        db.delete_table(u'home_blogpost')


    models = {
        u'home.blogpost': {
            'Meta': {'ordering': "['date']", 'object_name': 'BlogPost'},
            'context': ('django.db.models.fields.CharField', [], {'max_length': '323232'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        }
    }

    complete_apps = ['home']