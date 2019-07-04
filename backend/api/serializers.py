from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import FileUpload

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class FileUploadSerializer(serializers.HyperlinkedModelSerializer):
    
    result = serializers.JSONField(True)

    class Meta:
        model = FileUpload
        fields = ('datafile','result')

    def clean_json(self, obj):
        return obj.result

class WordRecognitionSerializer(serializers.HyperlinkedModelSerializer):
    
    result = serializers.JSONField(True)

    class Meta:
        model = FileUpload
        fields = ('datafile','result')

    def clean_json(self, obj):
        return obj.result