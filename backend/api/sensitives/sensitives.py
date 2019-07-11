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
    def check_sensitiveWords(keywords):
        t = time.time()
        startTime = int(round(t * 1000))
        result = {}
        for index, row in settings.DF.iterrows():
            if keywords in row['内容']:
                result["firstType"] = row['大类']
                result["secondType"] = row['次类']
                result["keyword"] = keywords
                break;
        t = time.time()
        endTime = int(round(t * 1000))
        print(endTime - startTime)
        print("result:",result)
    if __name__ == '__main__':
        check_sensitiveWords("十八摸")	 
# def check_sensitiveWords(keywords):    
#     pwd = os.getcwd()
#     csvFile = os.path.join(pwd,"backend","api","sensitives","sensitiveWords.csv")
#     #keywords="天安門屠殺"
#     print ("keywords input: ", keywords)
#     file =open(csvFile,'r')
#     lines=file.readlines()
#     file.close()
#     row=[]#定义行数组
#     column=[]#定义列数组
#     rowNumber = 1
#     result = {}
#     t = time.time()
#     startTime = int(round(t * 1000))
#     for line in lines:
#         if keywords in line:            
#             arr = line.split(',')    
#             print ("the keywords you entered belongs to the following data: ",keywords)
#             result = {
#                 "firstType": arr[0],
#                 "secondType": arr[1],
#                 "keyword": keywords
#             }
#         rowNumber = rowNumber + 1
    
#     t = time.time()
#     endTime = int(round(t * 1000))
#     result["millisecond"]=endTime-startTime
#     print("result:",result)
#     return result
# if __name__ == '__main__':
# 	check_sensitiveWords("十八摸")	 