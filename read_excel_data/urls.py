import views
from django.conf.urls import patterns, url
from read_excel_data.views import easyuni

urlpatterns = patterns(
	"",
	url(
		r"^easyuni",
		easyuni.import_data_easyuni,
		name="read_data_easyuni"
	)
)
