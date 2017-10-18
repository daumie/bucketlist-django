from rest_framework import serializers
from django_bucketlist.models import Bucketlist, STYLE_CHOICES


class BucketlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bucketlist
        fields =('id', 'title', 'description', 'style')

