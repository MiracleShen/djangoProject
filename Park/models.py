from django.db import models


# Create your models here.
class Street(models.Model):
    StreetName = models.CharField(max_length=50, unique=True, verbose_name='街道名称')
    RecordDate = models.DateTimeField(auto_now_add=True, verbose_name='记录时间')
    UpdateDate = models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')
    Memo = models.TextField(default='无', verbose_name='备注')

    def __str__(self):
        return self.StreetName

    class Meta:
        verbose_name_plural = '街道管理'

class Park(models.Model):
    XY = models.CharField(max_length=50,null=True,verbose_name='坐标')
    Street = models.ForeignKey('Street',null=True,on_delete=models.CASCADE,verbose_name='街道')
    No = models.CharField(max_length=10,null=True,verbose_name='门牌号')
    ParkName = models.CharField(max_length=50, unique=True, verbose_name='园区名称')
    PM = models.ForeignKey('ParkManager', on_delete=models.CASCADE, verbose_name='园区管理员')
    RecordDate = models.DateTimeField(auto_now_add=True, verbose_name='记录时间')
    UpdateDate = models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')
    Memo = models.TextField(default='无', verbose_name='备注')

    def __str__(self):
        return self.ParkName

    class Meta:
        verbose_name_plural = '园区管理'


class ParkManager(models.Model):
    PMName = models.CharField(max_length=50, unique=True, verbose_name='园区管理员名称')
    RecordDate = models.DateTimeField(auto_now_add=True, verbose_name='记录时间')
    UpdateDate = models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')
    Memo = models.TextField(default='无', verbose_name='备注')

    def __str__(self):
        return self.PMName

    class Meta:
        verbose_name_plural = '园区管理员'

class ParkLog(models.Model):
    Park = models.ForeignKey('Park',on_delete=models.CASCADE,verbose_name='园区')
    Title = models.CharField(max_length=50,verbose_name='标题')
    Content = models.TextField(null=True,verbose_name='内容')
    RecordDate = models.DateTimeField(auto_now_add=True, verbose_name='记录时间')
    UpdateDate = models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')
    Memo = models.TextField(default='无', verbose_name='备注')

    class Meta:
        verbose_name_plural = '开发日志'
