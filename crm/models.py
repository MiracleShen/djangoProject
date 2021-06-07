from django.db import models


# Create your models here.
class ContactHistory(models.Model):
    Name = models.CharField(max_length=20, verbose_name='姓名')
    ContactDateTime = models.DateTimeField(verbose_name='联系时间')
    ContactMedia = models.CharField(max_length=20, verbose_name='联系方式')
    Memo = models.TextField(verbose_name='联系内容')

    class Meta:
        verbose_name_plural = '联系记录'


class Contacts(models.Model):
    Name = models.CharField(max_length=20, verbose_name='姓名')
    Mobile = models.IntegerField(verbose_name='手机号')
    Email = models.EmailField(verbose_name='电子邮件')
    Memo = models.TextField(verbose_name='备注')

    class Meta:
        verbose_name_plural = '联系人'


class Organization(models.Model):
    OrganizeName = models.CharField(max_length=60, verbose_name='组织名称')
    OrganizeID = models.CharField(max_length=60, unique=True, verbose_name='组织代码')
    Memo = models.TextField(verbose_name='备注')

    def __str__(self):
        return self.OrganizeName

    class Meta:
        verbose_name_plural = '组织'
