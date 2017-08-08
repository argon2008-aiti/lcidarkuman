from django.conf.urls import include, url
from django.contrib import admin
import bussels_app
import info_system

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    # Examples:
    # url(r'^$', 'lcidarkuman.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^bussels/', include('bussels_app.urls', namespace="bussel")),
    url(r'^info/', include('info_system.urls', namespace="info")),
    url(r'^pastoral/', include('pastoral_care.urls', namespace="pastoral")),
    url(r'^notice/', include('notice_board.urls', namespace="noticeboard")),
    url(r'^finance/', include('treasury.urls', namespace="finance")),
    url(r'^events/', include('events_calendar.urls', namespace="events")),
    url(r'^json/', include('bussels_app.urls', namespace="ajax")),
    url(r'^under_development/', bussels_app.views.SectionUnderDevelopment.as_view(), name="under-dev"),
    url(r'^$', bussels_app.views.SectionUnderDevelopment.as_view(), name="under-dev"),
    url(r'^access_denied/', bussels_app.views.AccessDenied.as_view(), name="access-denied"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('django.contrib.auth.urls')),
]

