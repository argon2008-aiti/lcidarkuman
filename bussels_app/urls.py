from django.conf.urls import url
from django.contrib.auth import views
from django.views.generic import TemplateView
from views import *

urlpatterns = [
    url(r'^all/$', BusselListView.as_view(), name="all-bussels"),
    url(r'^authenticate/$', authenticate_bussel_request, name="bussel-authenticate"),
    url(r'^change/password/$', change_bussel_password, name="bussel-password-change"),
    url(r'^update/location/$', update_bussel_location, name="bussel-update-location"),
    url(r'^reports/all$', BusselReportListView.as_view(), name="all-bussel-reports"),
    url(r'^reports/all/export$', export_bussels_list, name="all-bussel-export"),
    url(r'^reports/month/export$', export_bussel_monthly_reports, name="monthly-bussel-export"),
    url(r'^reports/headers/all/json/$', bussell_reports_header_json, name="all-bussel-header-list"),
    url(r'^reports/details/(?P<pk>\d+)/$', BusselReportEditView.as_view(), name="bussel-report-detail"),
    url(r'^all/json/$', json_bussel_list, name="all-bussels-json"),
    url(r'^reports/all/json$', json_bussel_reports_list, name="all-bussel-reports-json"),
    url(r'^reports_for_bussel/all/$', get_reports_for_bussel, name="reports-for-bussel"),
    url(r'^bussel_reports/all/export$', export_bussel_reports, name="bussel-reports-export"),
    url(r'^details/(?P<pk>\d+)/$', BusselDetailView.as_view(), name="bussel-detail"),
    url(r'^report/save/$', save_bussel_report, name="bussel-report-save"),
]
