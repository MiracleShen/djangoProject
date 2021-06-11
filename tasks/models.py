import datetime

from django.db import models

# Create your models here.
from django.db import models
from django.utils.html import format_html

class Status(models.TextChoices):
    UNSTARTED = '未开始', "未开始"
    ONGOING = '进行中', "进行中"
    FINISHED = '已完成', "已完成"
    CANCEL = '已取消', '已取消'


class Tasktype(models.TextChoices):
    FIN = '账务管理', "账务管理"
    ADMIN = '行政管理', "行政管理"
    CS = '客户服务', "客户服务"
    TS = '技术支持', "技术支持"
    SM = '系统维护', "系统维护"
    RD = '软件开发', "软件开发"
    CO = '合伙人管理', "合伙人管理"


class Task(models.Model):
    tasktype = models.CharField(verbose_name='任务类型', default='账务管理', max_length=8, choices=Tasktype.choices)
    name = models.CharField(verbose_name="任务名称", max_length=65, unique=True)
    content = models.TextField(verbose_name="任务内容", default=" ")
    status = models.CharField(verbose_name="状态", max_length=8, choices=Status.choices)
    createdtime = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updatedtime = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    Creator = models.CharField(verbose_name='创建人', default='沈承永', max_length=40)

    def short_content(self):

        if len(str(self.content)) > 60:

            return '{}...'.format(str(self.content)[0:60])

        else:

            return str(self.content)

    short_content.short_description = u"内容"

    def colored_status(self):
        if self.status == '已完成':
            color_code = 'green'
        elif self.status == '进行中':
            color_code = 'orange'
        elif self.status == '未开始':
            color_code = 'red'
        elif self.status == '已取消':
            color_code = 'blue'
        else:
            color_code = 'black'
        return format_html(
            '<span style="color: {};">{}</span>',
            color_code,
            self.status,
        )

    colored_status.short_description = u"状态"

    def get_absolute_url(self):
        return {'assign_task': self.name}

    class Meta:
        verbose_name_plural = '任务管理'
        permissions = (
            ('assign_task', '分配任务'),
        )





# Create your models here.

