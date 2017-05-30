from django.conf.urls import url
from views import *

urlpatterns = [
    url('^all/json/$', notice_list_json, name='notice-list-json'),
    url('^add/$', add_notice, name='add-notice')
]
