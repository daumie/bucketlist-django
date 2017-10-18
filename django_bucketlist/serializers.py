from rest_framework import serializers
from django_bucketlist.models import Bucketlist, STYLE_CHOICES
from django.contrib.auth.models import User


class BucketlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bucketlist
        fields =('id', 'title', 'description', 'style', 'owner')
        owner = serializers.ReadOnlyField(source='owner.username')

class UserSerializer(serializers.ModelSerializer):
    bucketlist = serializers.PrimaryKeyRelatedField(many=True, queryset=Bucketlist.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'bucketlist')

