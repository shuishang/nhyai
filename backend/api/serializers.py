from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import FileUpload, FileImageTerrorismUpload, FileVisionPornUpload
from .models import VideoFileUpload,AudioFileUpload

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

class OcrGeneralSerializer(serializers.HyperlinkedModelSerializer):

    result = serializers.JSONField(True)

    class Meta:
        model = FileUpload
        fields = ('datafile','result')

    def clean_json(self, obj):
        return obj.result

class OcrIDCardSerializer(serializers.HyperlinkedModelSerializer):

    result = serializers.JSONField(True)

    class Meta:
        model = FileUpload
        fields = ('datafile','result')

    def clean_json(self, obj):
        return obj.result


class FileImageTerrorismUploadSerializer(serializers.HyperlinkedModelSerializer):
    result1 = serializers.JSONField(True)

    class Meta:
        model = FileImageTerrorismUpload
        fields = ('datafile1', 'result1')

    def clean_json(self, obj):
        return obj.result1


class FileVisionPornUploadSerializer(serializers.HyperlinkedModelSerializer):
    result2 = serializers.JSONField(True)

    class Meta:
        model = FileVisionPornUpload
        fields = ('datafile2', 'result2')

    def clean_json(self, obj):
        return obj.result2

class VideoFileUploadSerializer(serializers.HyperlinkedModelSerializer):
    
    result = serializers.JSONField(True)

    class Meta:
        model = VideoFileUpload
        fields = ('datafile','width','height','duration','count', 'result')

    def clean_json(self, obj):
        return obj.result

class AudioFileUploadSerializer(serializers.HyperlinkedModelSerializer):
    
    result = serializers.JSONField(True)

    class Meta:
        model = AudioFileUpload
        fields = ('datafile', 'result')

    def clean_json(self, obj):
        return obj.result