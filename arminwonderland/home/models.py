from django.db import models
from tinymce.models import HTMLField
from ckeditor.fields import RichTextField


class TechnicalWriting(models.Model):
	title = models.CharField(max_length=1024, verbose_name = u'Baslik')
	content = RichTextField()
	publish_date = models.DateField(verbose_name = u'Yayimlandigi Tarih')

	def __unicode__(self):
		return u'%s' % (self.title)

	class Meta:
		ordering = ["publish_date"]
		verbose_name = u"Teknik Yazi"
		verbose_name_plural = u"Teknik Yazilar"


class Contacts(models.Model):
	name = models.CharField(max_length=64, verbose_name = u'Contact Name', blank=False)
	email = models.EmailField(max_length=32, verbose_name = u'Contact Email', blank=False)
	content = models.TextField(max_length=1024, verbose_name = u'Reason', blank=True)
	date = models.DateTimeField(verbose_name = u'Date', blank=False)

		
	def __unicode__(self):
		return u'%s %s' % (self.name, self.email)

	class Meta:
		ordering = ["date"]
		verbose_name = "Contact"
		verbose_name_plural = "Contacts"