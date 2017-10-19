from django.conf.urls import url
from django.views.generic.base import RedirectView
from rest_framework.urlpatterns import format_suffix_patterns
from django_bucketlist import views

urlpatterns = [
    url(r'^bucketlists/$', views.BucketlistList.as_view(), name='bucketlist'),
    url(r'^$', RedirectView.as_view(pattern_name='bucketlist')),
    url(r'^bucketlists/(?P<pk>[0-9]+)/$', views.BucketlistDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)