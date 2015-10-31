from django.conf.urls import patterns, url, include

urlpatterns = patterns(
	"",
	url(
		r"^universities/",
		include('university.urls')
	),
	url(
		r"^read_excel_data/",
		include('read_excel_data.urls')
	)
)
