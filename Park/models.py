from django.db import models
from django.utils.html import format_html


class Park(models.Model):
    ParkName = models.CharField(max_length=50, unique=True, verbose_name='园区名称')
    Province = models.CharField(max_length=50, null=True, blank=True, verbose_name='省')
    City = models.CharField(max_length=50, null=True, blank=True, verbose_name='市')
    District = models.CharField(max_length=50, null=True, blank=True, verbose_name='区县')
    Street = models.CharField(max_length=50, null=True, blank=True, verbose_name='乡镇街道')
    Address = models.CharField(max_length=50, null=True, verbose_name='地址')
    PM = models.ForeignKey('ParkManager', on_delete=models.CASCADE, verbose_name='园区管理员')
    RecordDate = models.DateTimeField(auto_now_add=True, verbose_name='记录时间')
    UpdateDate = models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')
    Memo = models.TextField(default='无', verbose_name='备注')

    def __str__(self):
        return self.ParkName

    def pass_audit_str(self):
        parameter_str = 'id={}&Address={}'.format(str(self.id), str(self.Address))
        btn_str = '<a class="btn btn-xs btn-primary" href="{}">' \
                  '<input name="获取乡镇地址"' \
                  'type="button" id="passButton" ' \
                  'title="passButton" value="获取乡镇地址">' \
                  '</a>'
        return format_html(btn_str, '/Park/GetTown/?{}'.format(parameter_str))

    pass_audit_str.short_description = '获取乡镇地址'

    class Meta:
        verbose_name_plural = '园区'
        ordering=['id']

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
    Park = models.ForeignKey('Park', on_delete=models.CASCADE, verbose_name='园区')
    Title = models.CharField(max_length=50, verbose_name='标题')
    Content = models.TextField(null=True, verbose_name='内容')
    RecordDate = models.DateTimeField(auto_now_add=True, verbose_name='记录时间')
    UpdateDate = models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')
    Memo = models.TextField(default='无', verbose_name='备注')

    class Meta:
        verbose_name_plural = '开发历史'
