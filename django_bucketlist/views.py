from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django_bucketlist.models import Bucketlist
from django_bucketlist.serializers import BucketlistSerializer

#  Because we want to be able to POST to this view from clients
#  that won't have a CSRF token we need to mark the view as csrf_exempt
@csrf_exempt
def bucketlist_list(request):
    """
    List all bucket lists or create a bucketlist.
    """
    if request.method == 'GET':
        bucketlist = Bucketlist.objects.all()
        serializer = BucketlistSerializer(bucketlist, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BucketlistSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

# view which corresponds to an individual bucketlist

@csrf_exempt
def bucketlist_detail(request, pk):
    """
    Retrieve, update or delete a bucketlist.
    """
    try:
        bucketlist = Bucketlist.objects.get(pk=pk)
    except Bucketlist.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = BucketlistSerializer(bucketlist)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = BucketlistSerializer(bucketlist, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        bucketlist.delete()
        return HttpResponse(status=204)