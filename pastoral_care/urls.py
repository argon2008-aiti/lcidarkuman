from django.conf.urls import url
from django.views.generic import TemplateView
from views import *
from forms import *

urlpatterns = [
    url('^members/all/$', MemberShipListView.as_view(), name="all-members"),
    url('^members/details/(?P<pk>\d+)/$', MemberDetailView.as_view()),
    url('^members/edit/(?P<pk>\d+)/$', MemberEditView.as_view()),
    url('^members/all/json/$', json_member_list, name="all-members-json"),
    url('^members/new/$', AddNewMemberView.as_view(form_class=NewMemberForm), name="new-member"),
    url('^members/export$', export_members, name="export-members"),
    url('^attendance/authorize/$', authorize_attendance, name="authorize-attendance"),
    url('^attendance/start/$', start_attendance, name="start-attendance"),
    url('^attendance/finish/$', finish_attendance, name="finish-attendance"),
    url('^attendance/all/json/$', json_attendance_list, name="all-attendance-json"),
    url('^attendance/assigned/json/$', get_assigned_members, name="assigned-attendance-json"),
    url('^attendance/insession/details/$', get_attendance_insession_details, name="insession-details"),
    url('^attendance/submit/$', submit_attendance, name="attendance-submit"),
]
