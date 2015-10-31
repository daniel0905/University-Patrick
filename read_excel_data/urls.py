import views
from django.conf.urls import patterns, url
from read_excel_data.views import easyuni, cucas

urlpatterns = patterns(
	"",
	url(
		r"^easyuni",
		easyuni.import_data_easyuni,
		name="read_data_easyuni"
	),
	url(
		r"^cucas",
		cucas.import_data_cucas,
		name="read_data_cucas"
	)
)
