from django_bucketlist.models import Bucketlist
from django_bucketlist.serializers import BucketlistSerializer
from rest_framework import generics

class BucketlistList(generics.ListCreateAPIView):
    """
    List all bucket lists or create a bucketlist.
    """
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    
# view which corresponds to an individual bucketlist

class BucketlistDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a bucketlist instance.
    """
  
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer