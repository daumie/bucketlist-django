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

