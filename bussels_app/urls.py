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
    url(r'^performance$', BussellPerformanceMetricsView.as_view(), name="bussel-performance"),
    url(r'^performance/json/$', get_performance_data, name="bussell-performance-json"),
    url(r'^performance/monthly_average/json/$', get_monthly_average, name="bussell-performance-monthly-json"),
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
    url(r'^report/check/$', check_attendance_status, name="bussel-report-check"),
    url(r'^member/save/$', save_bussell_member, name="bussel-member-save"),
    url(r'^members/get/all/$', get_all_bussell_members, name="bussel-members-all"),
    url(r'^report/attendance/all/$', get_members_attendance_for_report, name="bussell-report-attendance"),
    url(r'^profile/save/$', update_bussell_profile, name="bussel-profile-save"),
    url(r'^profile/get/$', get_bussell_group_pic_url, name="bussel-profile-get"),
]
