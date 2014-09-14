from django.db import models
from tinymce.models import HTMLField

class BlogPost(models.Model):
	title = models.CharField(max_length=1024, verbose_name = u'Baslik')
	context = HTMLField()
	date = models.DateField(verbose_name = u'Yayimlandigi Tarih')

	def __unicode__(self):
		return u'%s' % (self.title)

	class Meta:
		ordering = ["date"]
		verbose_name = "Blog Postu"
		verbose_name_plural = "Blog Postlari"


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