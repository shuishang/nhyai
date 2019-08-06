# usr/bin/env python
# -*- coding: utf-8 -*-
import re
import time
import sys
import csv
import pandas as pd
import numpy as np
import datetime
import time
import random
import requests
import os
import codecs
import mmap
import contextlib
from django.conf import settings

class sensitiveClass:
    def __init__(self):
        self = self

    def check_sensitiveWords_test(self, df, input_word):
        t = time.time()
        startTime = int(round(t * 1000))
        temp_flag = 0 #敏感词临时标记
        sensitive_hit_flag = 0 #0-五敏感词  1-有敏感词
        sensitive_list = [] #敏感词列表
        sensitive_size = 0    #敏感词数量
        web_text = "<div>"
        if input_word != None:
            keywords = input_word.split(' ')
        
        for keyword in keywords:
            print("33333333333=",keyword)
            for index, row in df.iterrows():
                sensitiveCms = row['内容'].split('、')
                if keyword in sensitiveCms:
                    result = {}
                    result["firstType"] = row['大类']
                    result["secondType"] = row['次类']
                    result["keyword"] = keyword
                    temp_flag = 1
                    sensitive_hit_flag = 1
                    sensitive_size = sensitive_size + 1
                    sensitive_list.append(result)
                    
            if (temp_flag == 1):
                web_text = web_text + "<a class='red_txt'>" +keyword +"&nbsp;</a>"
            else:
                web_text = web_text + keyword+"&nbsp;"
            temp_flag = 0
        web_text = web_text + "</div>"
        t = time.time()
        endTime = int(round(t * 1000))
        print(endTime - startTime)
        resultMap = {} 
        resultMap["sensitive_hit_flag"] = sensitive_hit_flag
        resultMap["sensitive_size"] = sensitive_size
        resultMap["sensitive_list"] = sensitive_list
        resultMap["web_text"] = web_text
        print("resultMap:",resultMap)
        return resultMap

    def check_sensitiveWords(self, input_word):
        t = time.time()
        startTime = int(round(t * 1000))
        temp_flag = 0 #敏感词临时标记
        sensitive_hit_flag = 0 #0-五敏感词  1-有敏感词
        sensitive_list = [] #敏感词列表
        sensitive_size = 0    #敏感词数量
        web_text = "<div>"
        if input_word != None:
            keywords = input_word.split(' ')
        
        for keyword in keywords:
            for index, row in settings.DF.iterrows():                
                sensitiveCms = row['内容'].split('、')
                if keyword in sensitiveCms:
                    result = {}
                    result["firstType"] = row['大类']
                    result["secondType"] = row['次类']
                    result["keyword"] = keyword
                    temp_flag = 1
                    sensitive_hit_flag = 1
                    sensitive_size = sensitive_size + 1
                    sensitive_list.append(result)
            if (temp_flag == 1):
                web_text = web_text + "<a class='red_txt'>" +keyword +"&nbsp;</a>"
            else:
                web_text = web_text + keyword+"&nbsp;"
            temp_flag = 0
        web_text = web_text + "</div>"
        t = time.time()
        endTime = int(round(t * 1000))
        print(endTime - startTime)
        #print("result:",result)
        resultMap = {} 
        resultMap["sensitive_hit_flag"] = sensitive_hit_flag
        resultMap["sensitive_size"] = sensitive_size
        resultMap["sensitive_list"] = sensitive_list
        resultMap["web_text"] = web_text
        print("resultMap:",resultMap)
        return resultMap

if __name__ == '__main__':
    df = pd.read_csv(os.path.join(os.getcwd(),"backend","api","sensitives","sensitiveWords.csv"),encoding='gbk')
    sensitiveClass().check_sensitiveWords_test(df, "sssss 十八摸 十八摸 强奸")
    #sensitiveClass().check_sensitiveWords_test(df, "你 不是 跟 我 讲的 笑话 吗 欲死欲仙 十八摸")