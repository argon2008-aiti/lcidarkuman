from django.conf.urls import include, url
from django.contrib import admin

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    # Examples:
    # url(r'^$', 'lcidarkuman.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^bussels/', include('bussels_app.urls', namespace="bussel")),
    url(r'^json/', include('bussels_app.urls', namespace="ajax")),
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += staticfiles_urlpatterns()
