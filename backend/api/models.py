from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers
from django.utils.timezone import datetime
from uuid import uuid4
import os

# Create your models here.

def path_and_rename(instance, filename):
    upload_to = 'photos'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)


class FileUpload(models.Model):
    # datafile = models.ImageField(upload_to='photos')
    datafile = models.ImageField(upload_to=path_and_rename, max_length=255, null=True, blank=True)
    result = models.TextField(max_length=256,default='')


class FileImageTerrorismUpload(models.Model):
    # datafile = models.ImageField(upload_to='photos')
    datafile1 = models.ImageField(upload_to=path_and_rename, max_length=255, null=True, blank=True)
    result1 = models.TextField(max_length=256,default='')


class FileVisionPornUpload(models.Model):
    # datafile = models.ImageField(upload_to='photos')
    datafile2 = models.ImageField(upload_to=path_and_rename, max_length=255, null=True, blank=True)
    result2 = models.TextField(max_length=256,default='')

class WordRecognition(models.Model):
    datafile = models.ImageField(upload_to=path_and_rename, max_length=255, null=True, blank=True)
    result = models.TextField(max_length=255,default='')