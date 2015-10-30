import views
from django.conf.urls import patterns, url

urlpatterns = patterns(
	"",
	url(
		r"^",
		views.ListUniversity.as_view(),
		name="list_university"
	)
)
