from django.db import models
from django.utils.html import format_html

CONTACT_TYPE = (
    ('客户->我', '客户->我'),
    ('我->客户', '我->客户'),
)


class ContactHistory(models.Model):
    Contact = models.ForeignKey('Contacts', on_delete=models.CASCADE, verbose_name='姓名')
    ContactType = models.CharField(max_length=8, default='客户->我', choices=CONTACT_TYPE, verbose_name='联系类型', null=True)
    Memo = models.TextField(null=True, verbose_name='联系内容')
    ContactDateTime = models.DateTimeField(auto_now_add=True, verbose_name='联系时间')
    # ContactMedia = models.CharField(null=True, max_length=20, verbose_name='联系方式')
    Creator = models.CharField(verbose_name='创建人', default='沈承永', max_length=40)

    class Meta:
        verbose_name_plural = '联系记录'

    def colored_ContactType(self):
        if self.ContactType == '客户->我':
            color_code = 'red'
        elif self.ContactType == '我->客户':
            color_code = 'green'
        else:
            color_code = 'orange'
        return format_html(
            '<span style="color: {};">{}</span>',
            color_code,
            self.ContactType,
        )

    colored_ContactType.short_description = u"联系类型"


class Contacts(models.Model):
    Organize = models.ForeignKey('Organization', on_delete=models.CASCADE, default='1', verbose_name='客户名称')
    Name = models.CharField(max_length=20, verbose_name='姓名')
    Mobile = models.CharField(max_length=11,null=True, verbose_name='手机号')
    Email = models.EmailField(null=True, verbose_name='电子邮件')
    Memo = models.TextField(null=True, verbose_name='备注')

    def __str__(self):
        return self.Name + '||' + self.Organize.OrganizeName

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

class Oblist(models.Model):
    Campaign = models.CharField(max_length=20, verbose_name='战役')
    Name = models.CharField(max_length=50, verbose_name='名称')
    Phone1 = models.CharField(max_length=50,verbose_name='号码1')
    Phone2 = models.CharField(max_length=50,null=True, verbose_name='号码2')
    Status = models.CharField(max_length=20,default='未联系',verbose_name='状态')
    Memo = models.TextField(null=True, verbose_name='备注')
    class Meta:
        verbose_name_plural = '外呼名单'