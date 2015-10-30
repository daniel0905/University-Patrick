import models
from django.views.generic import ListView


class ListUniversity(ListView):
	template_name = "university/list.html"

	def get_queryset(self):
		# For search with keyword
		keyword = str(self.request.GET.get("search_courses_requirement", ""))

		if keyword:
			'''For search with keyword'''
			keyword_array = keyword.split(",")
			universities_id = []
			courses = models.Course.objects.all()

			# Check courses in entry requirement
			for c in courses:
				for k in keyword_array:
					key = k.strip("")
					if c.academic_requirement.find(key) > 0:
						if c.university.id not in universities_id:
							universities_id.append(c.university.id)
							break
			queryset = models.University.objects.filter(id__in=universities_id)
		else:
			'''For Universities default page'''
			queryset = models.University.objects.all()
		return queryset
