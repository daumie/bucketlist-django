from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_bucketlist.models import Bucketlist
from django_bucketlist.serializers import BucketlistSerializer

#  Because we want to be able to POST to this view from clients
#  that won't have a CSRF token we need to mark the view as csrf_exempt
@api_view(['GET', 'POST'])
def bucketlist_list(request, format=None):
    """
    List all bucket lists or create a bucketlist.
    """
    if request.method == 'GET':
        bucketlists = Bucketlist.objects.all()
        serializer = BucketlistSerializer(bucketlists, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BucketlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# view which corresponds to an individual bucketlist

@api_view(['GET', 'PUT', 'DELETE'])
def bucketlist_detail(request, pk, format=None):
    """
    Retrieve, update or delete a bucketlist.
    """
    try:
        bucketlist = Bucketlist.objects.get(pk=pk)
    except Bucketlist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BucketlistSerializer(bucketlist)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BucketlistSerializer(bucketlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        bucketlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)