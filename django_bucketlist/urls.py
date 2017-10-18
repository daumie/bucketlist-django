from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django_bucketlist import views

urlpatterns = [
    url(r'^bucketlists/$', views.BucketlistList.as_view()),
    url(r'^bucketlists/(?P<pk>[0-9]+)/$', views.BucketlistDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)