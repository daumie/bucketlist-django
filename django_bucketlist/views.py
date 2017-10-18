from django_bucketlist.models import Bucketlist
from django_bucketlist.serializers import BucketlistSerializer
from rest_framework import mixins
from rest_framework import generics

class BucketlistList(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     generics.GenericAPIView):
    """
    List all bucket lists or create a bucketlist.
    """
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# view which corresponds to an individual bucketlist

class BucketlistDetail(mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       generics.GenericAPIView):
    """
    Retrieve, update or delete a bucketlist instance.
    """
  
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
      return self.destroy(request, *args, **kwargs)