"""
created by: xiongjian
"""

from __future__ import print_function
import os
import argparse
import numpy as np
import pandas as pd
import time
import shutil
import uuid
import cv2
from PIL import Image
from io import BytesIO
import json
from .violence import check_violence
from PIL import Image
from tqdm import tqdm
import torch
from torch.utils.data import Dataset, DataLoader
from torch.autograd import Variable
import torchvision.models as models
from .util import ProtestDatasetEvalFile, modified_resnet50
from django.conf import settings
from decimal import Decimal
from decimal import getcontext
def get_two_float(f_str, n):
    f_str = str(f_str)      # f_str = '{}'.format(f_str) 也可以转换为字符串
    a, b, c = f_str.partition('.')
    c = (c+"0"*n)[:n]       # 如论传入的函数有几位小数，在字符串后面都添加n为小数0
    return ".".join([a, c])

def check_video(file_path):
    # 读取视频
    totalCount = 0
    pornTotalCount = 0
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
    os.makedirs(temp_path) #重新创建文件夹  
    contentList=[]
    violenceScoreArr = [0]*int(totalFrameNumber)
    pornScoreArr = [0]*int(totalFrameNumber)
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
            jsonResultInfo  = check_violence(temp_path + '/' +imageName)
            print(jsonResultInfo)
            violencePercent = jsonResultInfo.get('violence')
            violenceScore = float(violencePercent)
            pornPercent  = settings.NSFW.caffe_preprocess_and_compute_api(temp_path+imageName)
            violenceScoreArr[COUNT] = violenceScore
            pornScore = "%.2f" % float(pornPercent[1])
            pornScore = float(pornScore)
            #pornScore = "%.2f" % float(pornPercent[1])
            contentMap={}
            
            pornScoreArr[COUNT] = pornScore

            infoMap = {}
            infoMap['image_url'] = temp_path+imageName
            infoMap['sensitivity_time'] = get_two_float(COUNT / fps,2)
            infoMap['violence_sensitivity_level'] = get_two_float(violenceScore * 100,2)
            infoMap['porn_sensitivity_level'] = get_two_float(float(pornPercent[1]) * 100,2)
            #infoMap['politics_ sensitivity_level'] = 
            #infoMap['probability'] = 
            contentList.append(infoMap)

            COUNT = COUNT + 1
            #if COUNT>3:
            #    violencePercent=0
            # 延时一段33ms（1s?30帧）再读取下一帧，如果没有这一句便无法正常显示视频
            cv2.waitKey(33)
        cap.release()
        pornScoreArr = sorted(pornScoreArr)
        violenceScoreArr = sorted(violenceScoreArr)
        violence_sensitivity_level = 0
        if (violenceScoreArr[int(totalFrameNumber)-1] < 0.5):
            violence_sensitivity_level = 0
        if (violenceScoreArr[int(totalFrameNumber)-1] >= 0.5 and violenceScoreArr[int(totalFrameNumber)-1]<=0.9):
            violence_sensitivity_level = 1
        if (violenceScoreArr[int(totalFrameNumber)-1] > 0.9):
            violence_sensitivity_level = 2
        
        porn_sensitivity_level = 0
        if (pornScoreArr[int(totalFrameNumber)-1] < 0.5):
            porn_sensitivity_level = 0
        if (pornScoreArr[int(totalFrameNumber)-1] >= 0.5 and pornScoreArr[int(totalFrameNumber)-1]<=0.9):
            porn_sensitivity_level = 1
        if (pornScoreArr[int(totalFrameNumber)-1] > 0.9):
            porn_sensitivity_level = 2
        resultMap = {}
        resultMap['video_url'] = file_path
        resultMap['violence_sensitivity_level'] = violence_sensitivity_level
        resultMap['porn_sensitivity_level'] = porn_sensitivity_level
        resultMap['video_evidence_information'] = contentList
        #contentMap['politics_ sensitivity_level'] = 
        #shutil.rmtree(temp_path)
        #print(totalCount)

    else:
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
                violenceScore = float(violencePercent)
                pornPercent  = settings.NSFW.caffe_preprocess_and_compute_api(temp_path+imageName)
                pornScore = "%.2f" % float(pornPercent[1])
                pornScore = float(pornScore)                
                violenceScoreArr[COUNT] = violenceScore
                pornScoreArr[COUNT] = pornScore
                infoMap = {}
                infoMap['image_url'] = temp_path+imageName
                infoMap['sensitivity_time'] = get_two_float(COUNT / fps,2)
                infoMap['violence_sensitivity_level'] = get_two_float(violenceScore * 100,2)
                infoMap['porn_sensitivity_level'] = get_two_float(float(pornPercent[1]) * 100,2)
                #infoMap['politics_ sensitivity_level'] = 
                #infoMap['probability'] = 

                contentList.append(infoMap)
                COUNT = COUNT + 1
            c = c + 1
            cv2.waitKey(1)
            rval, frame = cap.read()
            violenceScoreArr = sorted(violenceScoreArr)
        cap.release()
        #判断暴恐图片
        violence_sensitivity_level = 0
        if (violenceScoreArr[int(totalFrameNumber)-1] < 0.5):
            violence_sensitivity_level = 0
        if (violenceScoreArr[int(totalFrameNumber)-1] >= 0.5 and violenceScoreArr[int(totalFrameNumber)-1]<=0.9):
            violence_sensitivity_level = 1
        if (violenceScoreArr[int(totalFrameNumber)-1] > 0.9):
            violence_sensitivity_level = 2
        

        #判断色情图片
        porn_sensitivity_level = 0
        if (pornScoreArr[int(totalFrameNumber)-1] < 0.5):
            porn_sensitivity_level = 0
        if (pornScoreArr[int(totalFrameNumber)-1] >= 0.5 and pornScoreArr[int(totalFrameNumber)-1]<=0.9):
            porn_sensitivity_level = 1
        if (pornScoreArr[int(totalFrameNumber)-1] > 0.9):
            porn_sensitivity_level = 2
        resultMap = {}
        resultMap['video_url'] = file_path
        resultMap['violence_sensitivity_level'] = violence_sensitivity_level
        resultMap['porn_sensitivity_level'] = porn_sensitivity_level
        resultMap['video_evidence_information'] = contentList
    
    return resultMap

    