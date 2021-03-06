# -- coding: utf-8 --


from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserMessage(models.Model):
    object_id = models.CharField(max_length=50,default="",blank=True,primary_key=True)
    name = models.CharField(max_length=20,verbose_name=u"用户名")
    email = models.EmailField(verbose_name=u"邮箱")
    address = models.CharField(max_length=100,verbose_name=u"地址")
    message = models.CharField(max_length=500,verbose_name=u"留言信息")

    class Meta:
        verbose_name = u"用户留言信息"
        verbose_name_plural = verbose_name  #复数信息
        # db_table = "uesr_message"
        # ordering = "-object_id"