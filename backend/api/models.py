from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers
from django.utils.timezone import datetime
from uuid import uuid4
import os
from django.utils.translation import gettext_lazy as _

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

def audiopath_and_rename(instance, filename):
    upload_to = 'audios'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

def video_and_rename(instance, filename):
    upload_to = 'videos'
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
    # datafile = models.ImageField(upload_to=path_and_rename, max_length=255, null=True, blank=True)
    # result1 = models.TextField(max_length=256,default='')
    image = models.FileField(upload_to=path_and_rename, max_length=255, null=True, blank=True)
    ret = models.IntegerField(_('ret'), null=True, blank=True)
    msg = models.TextField(max_length=255, default='')
    data = models.TextField(max_length=2048, default='')

class FileVisionPornUpload(models.Model):
    # datafile = models.ImageField(upload_to='photos')
    image = models.ImageField(upload_to=path_and_rename, max_length=255, null=True, blank=True)
    #result = models.TextField(max_length=256,default='')
    ret = models.IntegerField(_('ret'), null=True, blank=True)
    msg = models.TextField(max_length=255, default='')
    data = models.TextField(max_length=256, default='')

class WordRecognition(models.Model):
    text = models.CharField(_('text'), max_length=255, null=True, blank=True)
    sensitive_hit_flag = models.IntegerField(_('sensitive_hit_flag'), null=True, blank=True)
    sensitive_size = models.IntegerField(_('sensitive_size'), null=True, blank=True)
    sensitive_list = models.TextField(max_length=1024, default='')
    ret = models.IntegerField(_('ret'), null=True, blank=True)
    msg = models.TextField(max_length=255, default='')
    data = models.TextField(max_length=2048, default='')

class OcrGeneral(models.Model):
    image = models.ImageField(upload_to=path_and_rename, max_length=255, null=True, blank=True)
    ret = models.IntegerField(_('ret'), null=True, blank=True)
    msg = models.TextField(max_length=255, default='')
    data = models.TextField(max_length=255,default='')

class OcrIDCard(models.Model):
    image = models.ImageField(upload_to=path_and_rename, max_length=255, null=True, blank=True)
    #result = models.TextField(max_length=255,default='')
    ret = models.IntegerField(_('ret'), null=True, blank=True)
    msg = models.TextField(max_length=255, default='')
    data = models.TextField(max_length=2048, default='')

class VideoFileUpload(models.Model):
    # datafile = models.ImageField(upload_to='photos')
    video = models.FileField(upload_to=video_and_rename, max_length=255, null=True, blank=True)
    ret = models.IntegerField(_('ret'), null=True, blank=True)
    msg = models.TextField(max_length=255, default='')
    data = models.TextField(max_length=2048, default='')

class AudioFileUpload(models.Model):
    # datafile = models.ImageField(upload_to='photos')
    speech = models.FileField(upload_to=audiopath_and_rename, max_length=255, null=True, blank=True)
    #result = models.TextField(max_length=256,default='')
    ret = models.IntegerField(_('ret'), null=True, blank=True)
    msg = models.TextField(max_length=255, default='')
    data = models.TextField(max_length=2048, default='')

class AudioFileInspection(models.Model):
    # datafile = models.ImageField(upload_to='photos')
    speech = models.FileField(upload_to=audiopath_and_rename, max_length=255, null=True, blank=True)
    #result = models.TextField(max_length=256,default='')
    ret = models.IntegerField(_('ret'), null=True, blank=True)
    msg = models.TextField(max_length=255, default='')
    data = models.TextField(max_length=2048, default='')

class ImageFileUpload(models.Model):
    # datafile = models.ImageField(upload_to='photos')
    image = models.ImageField(upload_to=path_and_rename, max_length=255, null=True, blank=True)
    #result = models.TextField(max_length=256,default='')
    ret = models.IntegerField(_('ret'), null=True, blank=True)
    msg = models.TextField(max_length=255, default='')
    data = models.TextField(max_length=256, default='')
