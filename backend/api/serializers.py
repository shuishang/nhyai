from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import FileUpload, FileImageTerrorismUpload, FileVisionPornUpload
from .models import VideoFileUpload,AudioFileUpload,AudioFileInspection
from .models import WordRecognition,OcrGeneral,OcrIDCard

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

    ret = serializers.JSONField(True)
    msg = serializers.JSONField(True)
    data = serializers.JSONField(True)

    class Meta:
        model = WordRecognition
        fields = ('text','ret','msg','data')

    def clean_json(self, obj):
        return obj.ret,obj.msg,obj.data

class OcrGeneralSerializer(serializers.HyperlinkedModelSerializer):

    result = serializers.JSONField(True)

    class Meta:
        model = OcrGeneral
        fields = ('datafile','result')

    def clean_json(self, obj):
        return obj.result

class OcrIDCardSerializer(serializers.HyperlinkedModelSerializer):

    result = serializers.JSONField(True)

    class Meta:
        model = OcrIDCard
        fields = ('datafile','result')

    def clean_json(self, obj):
        return obj.result


class FileImageTerrorismUploadSerializer(serializers.HyperlinkedModelSerializer):
    result = serializers.JSONField(True)

    class Meta:
        model = FileImageTerrorismUpload
        fields = ('datafile', 'result')

    def clean_json(self, obj):
        return obj.result


class FileVisionPornUploadSerializer(serializers.HyperlinkedModelSerializer):
    result = serializers.JSONField(True)

    class Meta:
        model = FileVisionPornUpload
        fields = ('datafile', 'result')

    def clean_json(self, obj):
        return obj.result

class VideoFileUploadSerializer(serializers.HyperlinkedModelSerializer):
    
    data = serializers.JSONField(True)

    class Meta:
        model = VideoFileUpload
        fields = ('video','data','ret','msg')

    def clean_json(self, obj):
        return obj.data

class AudioFileUploadSerializer(serializers.HyperlinkedModelSerializer):
    
    result = serializers.JSONField(True)

    class Meta:
        model = AudioFileUpload
        fields = ('datafile', 'result')

    def clean_json(self, obj):
        return obj.result

class AudioFileInspectionSerializer(serializers.HyperlinkedModelSerializer):
    
    result = serializers.JSONField(True)

    class Meta:
        model = AudioFileInspection
        fields = ('datafile', 'result')

    def clean_json(self, obj):
        return obj.result