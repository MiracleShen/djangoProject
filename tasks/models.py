from django.db import models

# Create your models here.
from django.db import models


class Status(models.TextChoices):
    UNSTARTED = 'u', "未开始"
    ONGOING = 'o', "进行中"
    FINISHED = 'f',"已完成"


class Task(models.Model):
    name = models.CharField(verbose_name="任务名称", max_length=65, unique=True)
    content = models.TextField(verbose_name="任务内容",default=" ")
    status = models.CharField(verbose_name="状态", max_length=1, choices=Status.choices)

    def __str__(self):
        return self.name
