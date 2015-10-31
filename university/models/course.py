import logging
from django.db import models
from university import University


class Course(models.Model):

	class Meta:
		app_label = 'university'

	# ForeignKey to connect to University
	university = models.ForeignKey(University, null=True, blank=True)

	# Courses Information
	name = models.CharField(max_length="200", null=True, blank=True)
	level = models.CharField(max_length="200", null=True, blank=True)
	duration = models.CharField(max_length="100", null=True, blank=True)
	awarded_by = models.CharField(max_length="200", null=True, blank=True)
	study_mode = models.CharField(max_length="100", null=True, blank=True)

	about_course = models.TextField(null=True, blank=True)
	entry_requirements = models.TextField(null=True, blank=True)
	subjects = models.TextField(null=True, blank=True)

	# Fee Information
	tuition_fee_local_per_year = models.CharField(max_length="100", null=True, blank=True)
	tuition_fee_local_entire = models.CharField(max_length="100", null=True, blank=True)
	tuition_fee_inter_per_year = models.CharField(max_length="100", null=True, blank=True)
	tuition_fee_inter_entire = models.CharField(max_length="100", null=True, blank=True)
	other_costs = models.CharField(max_length="500", null=True, blank=True)

	# Living Cost
	accommodation_cost = models.CharField(max_length="200", null=True, blank=True)
	tuition_fee_living = models.CharField(max_length="200", null=True, blank=True)

	# Other Information
	qualification_awarded = models.CharField(max_length="200", null=True, blank=True)
	language = models.CharField(max_length="200", null=True, blank=True)
	starting_date = models.CharField(max_length="200", null=True, blank=True)
	application_deadline = models.CharField(max_length="200", null=True, blank=True)
	application_fee = models.CharField(max_length="200", null=True, blank=True)
	academic_requirement = models.CharField(max_length="200", null=True, blank=True)
	enrollment_quota = models.CharField(max_length="200", null=True, blank=True)
	affiliated_hospitals = models.TextField(null=True, blank=True)
	english_requirement = models.TextField(null=True, blank=True)
	admission_difficulty = models.TextField(null=True, blank=True)
	hsk_requirement = models.TextField(null=True, blank=True)
	application_materials = models.TextField(null=True, blank=True)

	def __unicode__(self):
		return self.name

	@classmethod
	def create_new_course(cls, **extra):
		try:
			return cls.objects.create(**extra)
		except Exception, e:
			logging.error(e)
			raise
