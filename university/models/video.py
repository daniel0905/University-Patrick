from django.db import models
from university import University


class Video(models.Model):

	class Meta:
		app_label = 'university'

	# ForeignKey to connect to University
	university = models.ForeignKey(University, null=True, blank=True)
	title = models.CharField(max_length="200", null=True, blank=True)
	url = models.CharField(max_length="200", null=True, blank=True)

	def __unicode__(self):
		return self.title
