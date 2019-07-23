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
    def __init__(self, df):
        self = self
        self.df = df

    def check_sensitiveWords_test(self, keywords):
        t = time.time()
        startTime = int(round(t * 1000))
        result = {}
        for index, row in self.df.iterrows():
            if keywords in row['内容']:
                result["firstType"] = row['大类']
                result["secondType"] = row['次类']
                result["keyword"] = keywords
                break
        t = time.time()
        endTime = int(round(t * 1000))
        print(endTime - startTime)
        print("result:",result)

    def check_sensitiveWords(self, keywords):
        t = time.time()
        startTime = int(round(t * 1000))
        result = {}
        for index, row in settings.DF.iterrows():
            if keywords in row['内容']:
                result["firstType"] = row['大类']
                result["secondType"] = row['次类']
                result["keyword"] = keywords
                break
        t = time.time()
        endTime = int(round(t * 1000))
        print(endTime - startTime)
        print("result:",result)

if __name__ == '__main__':
    df = pd.read_csv(os.path.join(os.getcwd(),"backend","api","sensitives","sensitiveWords.csv"),encoding='gbk')
    sensitiveClass(df).check_sensitiveWords_test("十八摸")