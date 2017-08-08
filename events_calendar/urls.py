from django.conf.urls import url
from django.views.generic import TemplateView
from views import *

urlpatterns = [
    url('^all/$', event_calendar_list_json, name="all-events"),
    url('^new/$', add_event_calendar, name="new-event"),
    url('^new/recurring/$', add_recurring_event, name="new-recurring-event")
]
