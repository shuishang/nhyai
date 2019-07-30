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
#from .ocr.chineseocr import OCR
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
from django.conf import settings

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

        bill_model = "通用OCR"
        file_path = iserializer.datafile.path
        # print (file_path)
        #check_result = OCR().getWordRecognition(file_path, bill_model)
        
        result = check_result
        serializer.save(result=check_result)

        return Response(status=status.HTTP_201_CREATED)

class OcrIDCardViewSet(viewsets.ModelViewSet):

    queryset = OcrIDCard.objects.all()
    serializer_class = OcrIDCardSerializer
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):

        print (self.request.data)
        iserializer = serializer.save()

        bill_model = "身份证"
        file_path = iserializer.datafile.path
        # print (file_path)
        #check_result = OCR().getWordRecognition(file_path, bill_model)
        
        result = check_result
        serializer.save(result=result)

        return Response(status=status.HTTP_201_CREATED)


class FileImageTerrorismUploadViewSet(viewsets.ModelViewSet):
    queryset = FileImageTerrorismUpload.objects.all()
    serializer_class = FileImageTerrorismUploadSerializer
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        print(self.request.data)
        iserializer = serializer.save()

        file_path = iserializer.datafile.path
        print(file_path)
        check_result = check_violence(file_path)
        # print (check_result)
        serializer.save(result=str(check_result))
        return Response(status=status.HTTP_201_CREATED)


class FileVisionPornUploadViewSet(viewsets.ModelViewSet):
        queryset = FileVisionPornUpload.objects.all()
        serializer_class = FileVisionPornUploadSerializer
        parser_classes = (MultiPartParser, FormParser,)

        def perform_create(self, serializer):
            print(self.request.data)
            iserializer = serializer.save()

            file_path = iserializer.datafile.path
            print(file_path)
            # check_result = vision_porn(file_path)
            scores = settings.NSFW.caffe_preprocess_and_compute_api(file_path)
            
            # print (check_result)
            serializer.save(result=str(scores[1]))
            return Response(status=status.HTTP_201_CREATED)

class VideoFileUploadViewSet(viewsets.ModelViewSet):
    queryset = VideoFileUpload.objects.all()
    serializer_class = VideoFileUploadSerializer
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        print(self.request.data)
        iserializer = serializer.save()
        totalCount = 0
        file_path = iserializer.video.path
        print (file_path)

        # 读取视频
        cap = cv2.VideoCapture(file_path)
        # 获取FPS(每秒传输帧数(Frames Per Second))
        fps = cap.get(cv2.CAP_PROP_FPS)
        # 获取总帧数
        totalFrameNumber = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        print("fps=",fps)
        print("totalFrameNumber=",totalFrameNumber)
        # 当前读取到第几帧
        COUNT = 0
        
        temp_path = settings.TEMP_PATH+str(uuid.uuid1())+"/"
        save_path = settings.SAVE_PATH+str(uuid.uuid1())+"/"
        os.makedirs(temp_path) #重新创建文件夹 
        os.makedirs(save_path) #重新创建文件夹 
        contentList=[]
        #violencePercent=1

        FPS_FLAG = settings.FPS_FLAG  #为True时，按帧读取；False时，按秒读取
        if FPS_FLAG:
            # 若小于总帧数则读一帧图像
            while COUNT < totalFrameNumber:
                contentMap={}
                # 一帧一帧图像读取
                ret, frame = cap.read()
                # 把每一帧图像保存成jpg格式（这一行可以根据需要选择保留）
                imageName = str(COUNT) + '.jpg'
                cv2.imwrite(temp_path+imageName, frame)
                # 显示这一帧地图像
                #cv2.imshow('video', frame)

                jsonResultInfo  = check_violence(temp_path+imageName)
                print(jsonResultInfo)
                violencePercent = jsonResultInfo.get('violence')
                
                #print(violencePercent)
                if violencePercent > 0.3:
                    totalCount = totalCount + 1
                    cv2.imwrite(save_path+imageName, frame)
                    #计算当前是第几秒
                    second = COUNT / fps
                    print("暴恐图片11222222222222")
                    print(second)
                    contentMap['image_url'] = save_path+imageName
                    contentMap['second'] = second
                    print(contentMap)
                    contentList.append(contentMap)

                else:
                    print("不是暴恐图片")

                COUNT = COUNT + 1
                #if COUNT>3:
                #    violencePercent=0
                # 延时一段33ms（1s?30帧）再读取下一帧，如果没有这一句便无法正常显示视频
                cv2.waitKey(33)
            cap.release()
            print(COUNT)
            print(contentList)
            shutil.rmtree(temp_path)
            print("删除成功1111111111111111")
            print(totalCount)

            serializer.save(result=contentList,video=file_path,duration=totalFrameNumber/fps,width=cap.get(3),height=cap.get(4),count=totalCount)
        else:
            print("666666666666666666666666")
            c = 1
            if cap.isOpened():  # 判断是否正常打开
                rval, frame = cap.read()
            else:
                rval = False
            timeF = fps  # 视频帧计数间隔频率
 
            while rval:  # 循环读取视频帧
                #pic_path = temp_path + '/'
                if (c % timeF == 0):  # 每隔timeF帧进行存储操作
                    imageName = str(COUNT) + '.jpg'
                    cv2.imwrite(temp_path + '/' + imageName, frame)#存储图像 
                    jsonResultInfo  = check_violence(temp_path + '/' +imageName)
                    print(jsonResultInfo)
                    violencePercent = jsonResultInfo.get('violence')
                    contentMap={}
                    #print(violencePercent)
                    if violencePercent > 0.1:
                        totalCount = totalCount + 1
                        cv2.imwrite(save_path+imageName, frame)
                        #计算当前是第几秒
                        print("暴恐图片333333333333333333")
                        contentMap['image_url'] = save_path+imageName
                        contentMap['second'] = c
                        print(contentMap)
                        contentList.append(contentMap)

                    else:
                        print("不是暴恐图片33333333333333")
                    COUNT = COUNT + 1
                c = c + 1
                cv2.waitKey(1)
                rval, frame = cap.read()
            cap.release()
            shutil.rmtree(temp_path)
            if (totalCount == 0):
                shutil.rmtree(save_path)
            print("删除成功3333333333333333")
            print(totalCount)

            serializer.save(result=contentList,video=file_path,duration=totalFrameNumber/fps,width=cap.get(3),height=cap.get(4),count=totalCount)
        
        
        # print (check_result)
        return Response(status=status.HTTP_201_CREATED)

class AudioFileUploadViewSet(viewsets.ModelViewSet):
    queryset = AudioFileUpload.objects.all()
    serializer_class = AudioFileUploadSerializer
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        print(self.request.data)
        iserializer = serializer.save()

        file_path = iserializer.datafile.path
        print(file_path)
        check_result = audio().getOneAudioContent(file_path)
        # print (check_result)
        serializer.save(result=str(check_result))
        return Response(status=status.HTTP_201_CREATED)

class AudioFileInspectionViewSet(viewsets.ModelViewSet):
    queryset = AudioFileInspection.objects.all()
    serializer_class = AudioFileInspectionSerializer
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        print(self.request.data)
        iserializer = serializer.save()

        file_path = iserializer.datafile.path
        print(file_path)
        audio_content = audio().getOneAudioContent(file_path)
        check_result = sensitiveClass().check_sensitiveWords(audio_content)
        # print (check_result)
        serializer.save(result=str(check_result))
        return Response(status=status.HTTP_201_CREATED)