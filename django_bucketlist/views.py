from django_bucketlist.models import Bucketlist
from django_bucketlist.serializers import BucketlistSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from django_bucketlist.serializers import UserSerializer
from rest_framework import permissions

class BucketlistList(generics.ListCreateAPIView):
    """
    List all bucket lists or create a bucketlist.
    """
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
# view which corresponds to an individual bucketlist

class BucketlistDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a bucketlist instance.
    """
  
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
