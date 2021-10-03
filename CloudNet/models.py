# Create your models here.
from django.db import models
from django.contrib import admin
from django.utils.html import format_html


class Card(models.Model):
    OPERATORS = (
        ('中国电信', '中国电信'),
        ('中国联通', '中国联通'),
        ('中国移动', '中国移动'),
        ('中国铁通', '中国铁通'),

    )
    CardNumber = models.CharField(max_length=19, unique=True, verbose_name='卡号')
    Device = models.ForeignKey('Device', null=True, verbose_name='设备', on_delete=models.SET_NULL)
    Operator = models.CharField(max_length=12, default='中国电信', verbose_name='运营商', choices=OPERATORS)
    RecordDate = models.DateTimeField(auto_now_add=True, verbose_name='记录时间')
    UpdateDate = models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')
    Memo = models.TextField(default='库存', verbose_name='备注')

    class Meta:
        verbose_name_plural = '物联网卡'


class Device(models.Model):
    TYPE = (
        ('YQ-212-OP', 'YQ-212-OP'),
        ('C3000', 'C3000'),
        ('C2000', 'C2000'),
        ('YQ-4001', 'YQ-4001'),
        ('YQ-4002', 'YQ-4002')
    )
    SN = models.CharField(max_length=19, null=True, verbose_name='SN码')
    Mac = models.CharField(max_length=17, unique=True, verbose_name='Mac地址')
    Type = models.CharField(max_length=12, default='YQ-212-OP', verbose_name='设备型号', choices=TYPE)
    RecordDate = models.DateTimeField(auto_now_add=True, verbose_name='记录时间')
    UpdateDate = models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')
    Memo = models.TextField(default='库存', verbose_name='备注')

    def __str__(self):
        return self.SN + "||" + self.Mac

    class Meta:
        verbose_name_plural = 'CPE设备'


class CloudNet(models.Model):
    Organize = models.ForeignKey('crm.Organization', null=True, verbose_name='客户', on_delete=models.SET_NULL)
    Device = models.ForeignKey('Device', null=True, verbose_name='设备', on_delete=models.SET_NULL)
    StartDate = models.DateField(verbose_name='开始时间')
    EndDate = models.DateField(verbose_name='结束时间')
    RecordDate = models.DateTimeField(auto_now_add=True, verbose_name='记录时间')
    UpdateDate = models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')
    Memo = models.TextField(default='库存', verbose_name='备注')

    class Meta:
        verbose_name_plural = '云宽带'


class Ticket(models.Model):
    TYPE = (
        ('新装', '新装'),
        ('维修', '维修'),
        ('加装', '加装'),
        ('拆机', '拆机'),
        ('其他', '其他')
    )
    WORKER = (
        ('胡开竹', '胡开竹'),
        ('刘梓妍', '刘梓妍'),
        ('其他', '其他')
    )
    Organize = models.ForeignKey('crm.Organization', null=True, verbose_name='客户', on_delete=models.SET_NULL)
    Title = models.CharField(max_length=30, verbose_name='工单名称')
    Type = models.CharField(max_length=12, default='新装', verbose_name='工单类型', choices=TYPE)
    Content = models.TextField(null=True, verbose_name='工单内容')
    Worker = models.CharField(max_length=12, default='胡开竹', verbose_name='施工人员', choices=WORKER)
    DateTime = models.DateTimeField(verbose_name='施工时间')
    RecordDate = models.DateTimeField(auto_now_add=True, verbose_name='记录时间')
    UpdateDate = models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')
    Memo = models.TextField(default='无', verbose_name='备注')

    class Meta:
        verbose_name_plural = '服务工单'
