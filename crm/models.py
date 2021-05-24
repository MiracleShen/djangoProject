from django.db import models


# Create your models here.

class Contacts(models.Model):
    Name = models.CharField(max_length=20, verbose_name='姓名')
    Mobile = models.IntegerField(verbose_name='手机号')
    Email = models.EmailField(verbose_name='电子邮件')
    Memo = models.TextField(verbose_name='备注')

    class Meta:
        verbose_name_plural = '联系人'


class Organization(models.Model):
    OrganizeName = models.CharField(max_length=60, verbose_name='组织名称')
    OrganizeID = models.CharField(max_length=60, verbose_name='组织代码')
    Memo = models.TextField(verbose_name='备注')

    class Meta:
        verbose_name_plural = '组织'
