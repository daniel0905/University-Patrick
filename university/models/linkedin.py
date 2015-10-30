from django.db import models
from university import University


class LinkedIn(models.Model):

	class Meta:
		app_label = 'university'

	# ForeignKey to connect to University
	university = models.ForeignKey(University, null=True, blank=True)
	group_linkedin = models.CharField(max_length="200", null=True, blank=True)
	title = models.CharField(max_length="200", null=True, blank=True)
	count = models.CharField(max_length="20", null=True, blank=True)

	def __unicode__(self):
		return self.title
