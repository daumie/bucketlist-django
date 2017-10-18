from rest_framework import serializers
from django_bucketlist.models import Bucketlist, STYLE_CHOICES


class BucketlistSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    description = serializers.CharField(style={'base_template': 'textarea.html'})
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        """
        Create and return a new `Bucketlist` instance, given the validated data.
        """
        return Bucketlist.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        update and return a new "Bucketlist" instance , given the validated data
        """
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance