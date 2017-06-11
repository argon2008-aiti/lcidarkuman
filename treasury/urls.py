from django.conf.urls import url
from django.contrib.auth import views
from django.views.generic import TemplateView
from views import *

urlpatterns = [
    url(r'^offering/all/$', get_all_offerings, name="offering-all"),
    url(r'^tithe/all/$', get_all_tithes, name="tithe-all"),
    url(r'^tithe/add/$', add_tithe, name="tithe-add"),
    url(r'^offering/add/$', add_offering, name="offering-add"),
]
