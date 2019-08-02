from django.contrib.auth.models import User, Group
from rest_framework import viewsets,views
from api.serializers import UserSerializer, GroupSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ParseError
# uload package
from rest_framework.parsers import MultiPartParser,FormParser
from .serializers import FileUploadSerializer,WordRecognitionSerializer,FileImageTerrorismUploadSerializer, FileVisionPornUploadSerializer,AudioFileUploadSerializer
from .models import FileUpload,WordRecognition,FileImageTerrorismUpload, FileVisionPornUpload
# Handle Image
from PIL import Image
from io import BytesIO
import json
from .violence import check_violence
from .video import check_video
from .ocr.chineseocr import OCR
from violentsurveillance.image_terrorism import image_terrorism
from violentsurveillance.vision_porn import vision_porn
from django.conf import settings
from .serializers import VideoFileUploadSerializer,OcrGeneralSerializer,OcrIDCardSerializer,AudioFileInspectionSerializer
from .models import VideoFileUpload,AudioFileUpload,OcrGeneral,OcrIDCard,AudioFileInspection
import os
import shutil
import uuid
import cv2
from .kaldi.audios import audio
from .sensitives.sensitives import sensitiveClass

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FileUploadViewSet(viewsets.ModelViewSet):
    
    queryset = FileUpload.objects.all()
    serializer_class = FileUploadSerializer
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        
        print(self.request.data)
        iserializer = serializer.save()
        # file_obj = self.request.data.get('datafile')
        # print (file_obj)
        # ...
        # do some stuff with uploaded file
        # ...
        # try:
        #     img = Image.open(file_obj)
        #     # img.verify()
        #     pic_io = BytesIO()
        #     img.save(pic_io,img.format)

        # except:
        #     raise ParseError("Unsupported image type")

        file_path = iserializer.datafile.path
        print(file_path)
        check_result = check_violence(file_path)
        # print (check_result)

        result = {
                "ret": 0,
                "msg": "ok",
                "data": {
                    "tag_list": [
                    {
                        "tag_name": "protest",
                        "probability": check_result['protest']
                    },
                    {
                        "tag_name": "violence",
                        "probability": check_result['violence']
                    },
                    {
                        "tag_name": "sign",
                        "probability": check_result['sign']
                    },
                    {
                        "tag_name": "photo",
                        "probability": check_result['photo']
                    },
                    {
                        "tag_name": "fire",
                        "probability": check_result['fire']
                    },
                    {
                        "tag_name": "police",
                        "probability": check_result['police']
                    },
                    {
                        "tag_name": "children",
                        "probability": check_result['children']
                    },
                    {
                        "tag_name": "group_20",
                        "probability": check_result['group_20']
                    },
                    {
                        "tag_name": "group_100",
                        "probability": check_result['group_100']
                    },
                    {
                        "tag_name": "flag",
                        "probability": check_result['flag']
                    },
                    {
                        "tag_name": "night",
                        "probability": check_result['night']
                    },
                    {
                        "tag_name": "shouting",
                        "probability": check_result['shouting']
                    }]
                }
            }
        serializer.save(result=result)

        return Response(status=status.HTTP_201_CREATED)

class WordRecognitionViewSet(viewsets.ModelViewSet):

    queryset = WordRecognition.objects.all()
    serializer_class = WordRecognitionSerializer
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):

        print (self.request.data)
        iserializer = serializer.save()

        text = iserializer.text
        print (text)
        sensitive_list = sensitiveClass().check_sensitiveWords(text)

        if sensitive_list.get('sensitive_hit_flag') == 0:
            ret = 1
            msg = "无匹配记录"
        else:
            ret = 0
            msg = "匹配到记录"

        data = sensitive_list
        serializer.save(ret=ret,msg=msg,data=data)

        return Response(status=status.HTTP_201_CREATED)

class OcrGeneralViewSet(viewsets.ModelViewSet):

    queryset = OcrGeneral.objects.all()
    serializer_class = OcrGeneralSerializer
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):

        print (self.request.data)
        iserializer = serializer.save()
        ret = 0
        msg = "成功"
        bill_model = "通用OCR"
        file_path = iserializer.datafile.path
        # print (file_path)
        check_result = OCR().getWordRecognition(file_path, bill_model)
        arr = check_result['res']
        dataArr = []
        for each in arr:
            dataArr.append(each["text"])
        #result = check_result
        serializer.save(data=dataArr,ret=ret,msg=msg)

        return Response(status=status.HTTP_201_CREATED)

class OcrIDCardViewSet(viewsets.ModelViewSet):

    queryset = OcrIDCard.objects.all()
    serializer_class = OcrIDCardSerializer
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):

        print (self.request.data)
        iserializer = serializer.save()
        ret = 0
        msg = "成功"
        bill_model = "身份证"
        file_path = iserializer.idcardImage.path
        # print (file_path)
        check_result = OCR().getWordRecognition(file_path, bill_model)
        arr = check_result['res']
        dataMap= {}
        for each in arr:
            dataMap[each['name']] = each['text']
        #result = check_result
        serializer.save(data=dataMap,ret=ret,msg=msg)

        return Response(status=status.HTTP_201_CREATED)


class FileImageTerrorismUploadViewSet(viewsets.ModelViewSet):
    queryset = FileImageTerrorismUpload.objects.all()
    serializer_class = FileImageTerrorismUploadSerializer
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        print(self.request.data)
        iserializer = serializer.save()
        ret = 0
        msg = "成功"
        file_path = iserializer.image.path
        print(file_path)
        check_result = check_violence(file_path)
        # print (check_result)
        violence = check_result['violence']
        resultMap = {}
        resultMap['violence'] = violence
        serializer.save(data=resultMap,ret=ret,msg=msg)
        return Response(status=status.HTTP_201_CREATED)


class FileVisionPornUploadViewSet(viewsets.ModelViewSet):
        queryset = FileVisionPornUpload.objects.all()
        serializer_class = FileVisionPornUploadSerializer
        parser_classes = (MultiPartParser, FormParser,)

        def perform_create(self, serializer):
            print(self.request.data)
            iserializer = serializer.save()
            ret = 0
            msg = "成功"
            file_path = iserializer.image.path
            print(file_path)
            # check_result = vision_porn(file_path)
            scores = settings.NSFW.caffe_preprocess_and_compute_api(file_path)
            resultMap = {}
            resultMap['normal_hot_porn'] = scores[1]
            # print (check_result)
            serializer.save(data=resultMap,ret=ret,msg=msg)
            return Response(status=status.HTTP_201_CREATED)

class VideoFileUploadViewSet(viewsets.ModelViewSet):
    queryset = VideoFileUpload.objects.all()
    serializer_class = VideoFileUploadSerializer
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        print(self.request.data)
        iserializer = serializer.save()
        file_path = iserializer.video.path
        print (file_path)
        resultMap = check_video(file_path)
        ret = 0
        msg = "成功"
        #serializer.save(result=contentList,video=file_path,duration=totalFrameNumber/fps,width=cap.get(3),height=cap.get(4),count=totalCount)
        serializer.save(data=resultMap,ret=ret,msg=msg)
        
        
        # print (check_result)
        return Response(status=status.HTTP_201_CREATED)

class AudioFileUploadViewSet(viewsets.ModelViewSet):
    queryset = AudioFileUpload.objects.all()
    serializer_class = AudioFileUploadSerializer
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        print(self.request.data)
        iserializer = serializer.save()
        ret = 0
        msg = "成功"
        file_path = iserializer.speech.path
        print(file_path)
        check_result = audio().getOneAudioContent(file_path)
        # print (check_result)
        resultMap ={}
        resultMap['text'] = check_result
        serializer.save(data=resultMap,ret=ret,msg=msg)
        return Response(status=status.HTTP_201_CREATED)

class AudioFileInspectionViewSet(viewsets.ModelViewSet):
    queryset = AudioFileInspection.objects.all()
    serializer_class = AudioFileInspectionSerializer
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        print(self.request.data)
        iserializer = serializer.save()
        ret = 0
        msg = "成功"
        file_path = iserializer.datafile.path
        print(file_path)
        audio_content = audio().getOneAudioContent(file_path)
        check_result = sensitiveClass().check_sensitiveWords(audio_content)
        # print (check_result)
        serializer.save(data=str(check_result),ret=ret,msg=msg)
        return Response(status=status.HTTP_201_CREATED)