from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django_bucketlist.models import Bucketlist
from django_bucketlist.serializers import BucketlistSerializer
from django.http import Http404

class BucketlistList(APIView):
    """
    List all bucket lists or create a bucketlist.
    """
    def get(self, request, format=None):
        bucketlists = Bucketlist.objects.all()
        serializer = BucketlistSerializer(bucketlists, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BucketlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# view which corresponds to an individual bucketlist

class BucketlistDetail(APIView):
    """
    Retrieve, update or delete a bucketlist instance.
    """
    def get_object(self, pk):
        try:
           return Bucketlist.objects.get(pk=pk)
        except Bucketlist.DoesNotExist:
            raise Http404

    def get(self, request, pk, format= None):
        bucketlist = self.get_object(pk)
        serializer = BucketlistSerializer(bucketlist)
        return Response(serializer.data)

    def put(self, request, pk, format= None):
        bucketlist = self.get_object(pk)
        serializer = BucketlistSerializer(bucketlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format= None):
        bucketlist = self.get_object(pk)
        bucketlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)