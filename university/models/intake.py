from django.db import models
from course import Course


class Intake(models.Model):

	class Meta:
		app_label = 'university'

	# ForeignKey to connect to Course
	course = models.ForeignKey(Course, null=True, blank=True)

	# Intake is determined by month
	month = models.IntegerField(null=True, blank=True)

	def __unicode__(self):
		return self.month
