from django.conf.urls import url
from django_bucketlist import views

urlpatterns = [
    url(r'^bucketlist/$', views.bucketlist_list),
    url(r'^bucketlist/(?P<pk>[0-9]+)/$', bucketlist_detail),
]