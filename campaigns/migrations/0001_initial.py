# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Campain'
        db.create_table(u'campaigns_campain', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('change_id', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=512)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('overview', self.gf('django.db.models.fields.TextField')()),
            ('signature_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('image_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'campaigns', ['Campain'])


    def backwards(self, orm):
        # Deleting model 'Campain'
        db.delete_table(u'campaigns_campain')


    models = {
        u'campaigns.campain': {
            'Meta': {'object_name': 'Campain'},
            'change_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'overview': ('django.db.models.fields.TextField', [], {}),
            'signature_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '512'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['campaigns']
