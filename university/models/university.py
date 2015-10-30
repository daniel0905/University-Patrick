from django.db import models


class University(models.Model):

	class Meta:
		app_label = 'university'

	# University Information
	name = models.CharField(max_length="200")
	about = models.TextField(null=True, blank=True)
	history = models.TextField(null=True, blank=True)
	year_founded = models.CharField(max_length="100", null=True, blank=True)

	# Student Information
	student_population = models.IntegerField(null=True, blank=True)
	student_sum = models.CharField(max_length="100", null=True, blank=True)
	male_female_ratio = models.CharField(max_length="20", null=True, blank=True)
	local_international_ratio = models.CharField(max_length="20", null=True, blank=True)
	alumni = models.TextField(null=True, blank=True)

	# Campus Information
	campus = models.TextField(null=True, blank=True)
	accommodation = models.TextField(null=True, blank=True)
	location_description = models.TextField(null=True, blank=True)

	# Social Network Link
	facebook_link = models.CharField(max_length="500", null=True, blank=True)
	twitter_link = models.CharField(max_length="500", null=True, blank=True)
	linkedin_link = models.CharField(max_length="500", null=True, blank=True)

	# Other Information
	awards = models.TextField(null=True, blank=True)
	disclaimer = models.TextField(null=True, blank=True)
	additional_info = models.TextField(null=True, blank=True)

	location = models.CharField(max_length="100", null=True, blank=True)
	detail_location = models.CharField(max_length="100", null=True, blank=True)
	acceptance_rate = models.IntegerField(null=True, blank=True)

	male = models.IntegerField(null=True, blank=True)
	gpa = models.CharField(max_length="20", null=True, blank=True)
	sat = models.CharField(max_length="20", null=True, blank=True)
	act = models.CharField(max_length="20", null=True, blank=True)

	application_fee = models.IntegerField(null=True, blank=True)
	os_net_price = models.IntegerField(null=True, blank=True)
	is_net_price = models.IntegerField(null=True, blank=True)
	is_tuition = models.IntegerField(null=True, blank=True)
	os_tuition = models.IntegerField(null=True, blank=True)
	living_expense = models.CharField(max_length="200", null=True, blank=True)

	housing_amount = models.IntegerField(null=True, blank=True)
	financial_aid = models.IntegerField(null=True, blank=True)
	apply_finaid_rate = models.IntegerField(null=True, blank=True)
	receive_finaid_rate = models.IntegerField(null=True, blank=True)

	def __unicode__(self):
		return self.name

