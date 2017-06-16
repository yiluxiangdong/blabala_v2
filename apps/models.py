#coding=utf-8
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=128,verbose_name='用户名')
    passwd = models.CharField(max_length=128, verbose_name='密码')
    passwd2 = models.CharField(max_length=128, verbose_name='重复密码')
    email = models.EmailField(verbose_name='邮箱')
    phone = models.CharField(max_length=128,verbose_name='手机号')
    verticode = models.CharField(max_length=128, verbose_name='手机号')
    def __unicode__(self):
        return self.name