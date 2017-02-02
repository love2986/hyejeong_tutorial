from django.conf.urls import url, include
from django.contrib import admin
from blog import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<pk>\d+)/comments/new/$', views.comment_new, name='comment_new'),
]
