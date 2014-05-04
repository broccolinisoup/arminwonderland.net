from django.db import models

# Create your models here.

class BlogPost(models.Model):
	title = models.CharField(max_length=32, verbose_name = u'Baslik')
	context = models.CharField(max_length=323232, verbose_name = u'Icerik')
	date = models.DateField(verbose_name = u'Yayimlandigi Tarih')

	def __unicode__(self):
		return u'%s' % (self.title)

	class Meta:
		ordering = ["date"]
		verbose_name = "Blog Postu"
		verbose_name_plural = "Blog Postlari"

