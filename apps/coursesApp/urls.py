from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses$', views.index),
    url(r'^destroy/(?P<id>\d+)$', views.delete_page),
    url(r'^show/(?P<id>\d+)$', views.course_page),

    url(r'^add$', views.add_process),
    url(r'^delete/(?P<id>\d+)$', views.delete_process),
    url(r'^add_comment/(?P<id>\d+)$', views.add_comment),

]
