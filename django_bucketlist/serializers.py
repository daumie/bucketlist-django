from rest_framework import serializers
from django_bucketlist.models import Bucketlist, Item
from django.contrib.auth.models import User


class BucketlistSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Bucketlist
        fields =('id', 'title', 'description', 'owner')

class UserSerializer(serializers.ModelSerializer):
    bucketlist = serializers.PrimaryKeyRelatedField(many=True, queryset=Bucketlist.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'bucketlist')

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ('title', 'description', 'bucketlist')