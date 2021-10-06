from django.db import models
from django.utils.html import format_html
# Create your models here.

class OWNERS(models.TextChoices):
    MIR = '沈承永', '沈承永'
    GMM = '耿萌萌', '耿萌萌'
    WZM = '王志杰','王志杰'
class Status(models.TextChoices):
    AA = '未联系', '未联系'
    BB = '未接通', '未接通'
    CC = '拒绝沟通', '拒绝沟通'
    DD = '再联系', '再联系'
    EE = '有意向', '有意向'
    FF = '有需求', '有需求'
class Oblist(models.Model):
    Campaign = models.CharField(max_length=20, verbose_name='战役')
    Name = models.CharField(max_length=50, verbose_name='名称')
    Phone1 = models.CharField(max_length=50, verbose_name='号码1')
    Phone2 = models.CharField(blank=True,max_length=50, null=True, verbose_name='号码2')
    Status = models.CharField(max_length=20, default='未联系', verbose_name='状态', choices=Status.choices)
    Memo = models.TextField(null=True, verbose_name='备注')
    Owner = models.CharField(verbose_name='执行人', default='沈承永', max_length=40, choices=OWNERS.choices)
    def short_content(self):

        if len(str(self.Memo)) > 30:

            return '{}...'.format(str(self.Memo)[0:30])

        else:

            return str(self.Memo)

    short_content.short_description = u"备注"
    def colored_Status(self):
        if self.Status == '未联系' or self.Status== '未接通':
            color_code = 'blue'
        elif self.Status == '拒绝沟通':
            color_code = 'black'
        elif self.Status == '再联系':
            color_code = 'green'
        elif self.Status == '有意向':
            color_code = 'orange'
        elif self.Status == '有需求':
            color_code = 'red'
        else:
            color_code = 'black'
        return format_html(
            '<span style="color: {};">{}</span>',
            color_code,
            self.Status,
        )

    colored_Status.short_description = u"状态"
    class Meta:
        verbose_name_plural = '电话营销'