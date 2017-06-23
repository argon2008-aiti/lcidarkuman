from django.conf.urls import url
from django.contrib.auth import views
from django.views.generic import TemplateView
from views import *

urlpatterns = [
    url(r'^authenticate/$', log_in_shepherd, name="shepherd-login"),
    url(r'^authenticate/treasury/$', treasury_authenticate, name="treasury-authenticate"),
    url(r'^change/password/$', change_password, name="shepherd-password-change"),
]
