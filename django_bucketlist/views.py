from django_bucketlist.models import Bucketlist, Item
from django_bucketlist.serializers import BucketlistSerializer, ItemSerializer
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
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        """
         This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return Bucketlist.objects.filter(owner=user)
# view which corresponds to an individual bucketlist

class BucketlistDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a bucketlist instance.
    """
    queryset = Bucketlist.objects.filter()
    serializer_class = BucketlistSerializer
    permission_classes = (permissions.IsAuthenticated,)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ItemList(generics.ListCreateAPIView):
    """
    List all item lists or create a bucketlist.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):

        serializer.save()

    def get_queryset(self):
        """
         This view should return a list of all the items 
         for the curently authenticated user
        """
        user = self.request.user
        return Item.objects
# view which corresponds to an individual bucketlist

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a bucketlist instance.
    """
    queryset = Item.objects.filter()
    serializer_class = ItemSerializer
    permission_classes = (permissions.IsAuthenticated,)

class ItemListAll(generics.ListAPIView):
    """
    List all item lists or create a bucketlist.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):

        serializer.save()

    def get_queryset(self):
        """
         This view should return a list of all the items 
         for the curently authenticated user
        """
        user = self.request.user
        return Item.objects