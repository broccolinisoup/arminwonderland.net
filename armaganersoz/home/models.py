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

