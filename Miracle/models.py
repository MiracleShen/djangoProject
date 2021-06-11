from django.db import models

# Create your models here.
from django.db import models
from django.contrib import admin
from django.utils.html import format_html


# 关于号码的管理，主要在于当前号码是否可选、当前号码被谁占用了；当前号码开了几个并发（这个功能还需要EZUC+加以配合）
class MiracleNumber(models.Model):
    OPERATORS = (
        ('中国电信', '中国电信'),
        ('中国联通', '中国联通'),
        ('中国移动', '中国移动'),
        ('中国铁通', '中国铁通'),

    )
    STATUSS = (
        ('可选', '可选'),
        ('锁定', '锁定'),
        ('已售', '已售'),
    )
    Zip = models.CharField(max_length=4, default='021', verbose_name='区号')
    Number = models.IntegerField(verbose_name='固话号码')
    Operator = models.CharField(max_length=12, verbose_name='运营商', choices=OPERATORS)
    Status = models.CharField(max_length=8, verbose_name='状态', default='可选', choices=STATUSS)
    Organize =models.CharField(max_length=30,default=' ',verbose_name='客户名称')
    def colored_Status(self):
        if self.Status == '可选':
            color_code = 'green'
        elif self.Status == '锁定':
            color_code = 'orange'
        else:
            color_code = 'red'
        return format_html(
            '<span style="color: {};">{}</span>',
            color_code,
            self.Status,
        )

    colored_Status.short_description = u"状态"

    class Meta:
        unique_together = (("Zip", "Number"),)
        verbose_name_plural = 'Miracle码号'


class MiracleOrders(models.Model):
    CustomerName = models.CharField(max_length=40, verbose_name='客户名称')
    OrderDate = models.DateTimeField(verbose_name='下单时间')
    Number_0 = models.IntegerField(default=0, verbose_name='普通号码数')
    Number_1 = models.IntegerField(default=0, verbose_name='1星号码数')
    Number_2 = models.IntegerField(default=0, verbose_name='2星号码数')
    Number_3 = models.IntegerField(default=0, verbose_name='3星号码数')
    Number_4 = models.IntegerField(default=0, verbose_name='4星号码数')
    Number_5 = models.IntegerField(default=0, verbose_name='5星号码数')
    Line_Number = models.IntegerField(default=0, verbose_name='并发数')
    PBX_Type = models.CharField(max_length=10, verbose_name='交换机类型')
    MCU_Type = models.CharField(max_length=10, verbose_name='多方通话许可')
    API_Type = models.CharField(max_length=10, verbose_name='API许可')
    APP_Number = models.IntegerField(verbose_name='APP许可数')
    SIP_Number = models.IntegerField(verbose_name='SIP许可数')
    Log_Number = models.IntegerField(verbose_name='录音许可数')
    CC_Number = models.IntegerField(verbose_name='轻客服许可数')
    HPR_Number = models.IntegerField(default=0, verbose_name='话机月租数量')  # 话机月租统一10元/月，WiFi话机，看长线

    class Meta:
        verbose_name_plural = 'Miracle订单'


# 话费账单，由EZUC+系统生成，每月月初手工录入到系统中
# 后期考虑系统自动从EZUC+抓取通话清单，系统自动计算生成月度账单到MiracleBill，用户也可以在系统中查询详单；实时的话单，还是要到服务器上去查看
class MiracleCredit(models.Model):
    CustomerID = models.ForeignKey('crm.Organization',default=1,on_delete=models.CASCADE,verbose_name='客户名称')
    Year = models.CharField(max_length=4, verbose_name='年份')
    Month = models.CharField(max_length=2, verbose_name='月份')
    Credit = models.FloatField(verbose_name='消费金额')
    RecordDate = models.DateTimeField(auto_now=True, verbose_name='记录时间')

    class Meta:
        verbose_name_plural = 'Miracle话单'


# 客户账单，目前由两部分生成，一部分是根据Miracle Order里的数据，每月自动计算生成月租费账单；另一部分是从EZUC+中获取每月话费账单，插入到Miracle Bill中。两者相加，就是用户当月应付的账单。
# 前期由慈俭运营人员每月月初手工生成账单发给客户，后期可以采用电子邮件的方式发送给客户的指定邮箱；或者短信、微信、电话的方式通知到用户的联系人，并告知对方付费。
class MiracleBill(models.Model):
    BILL_TYPE = (
        ('租金', '租金'),
        ('话费', '话费'),
    )
    CustomerID = models.ForeignKey('crm.Organization',on_delete=models.CASCADE,verbose_name='客户名称')
    Year = models.CharField(max_length=4, verbose_name='年份')
    Month = models.CharField(max_length=2, verbose_name='月份')
    Bill_Cycle = models.CharField(max_length=2, verbose_name='计费周期')
    Bill_Type = models.CharField(choices=BILL_TYPE,default='租金',max_length=2, verbose_name='账单类型')
    Bill = models.FloatField(verbose_name='账单金额')
    RecordDate = models.DateTimeField(auto_now=True, verbose_name='记录时间')
    Memo = models.TextField(default= '1',verbose_name='备注')
    def colored_Bill_Type(self):
        if self.Bill_Type == '租金':
            color_code = 'orange'
        elif self.Bill_Type == '话费':
            color_code = 'green'
        else:
            color_code = 'black'
        return format_html(
            '<span style="color: {};">{}</span>',
            color_code,
            self.Bill_Type,
        )
    colored_Bill_Type.short_description = u"账单类型"
    class Meta:
        verbose_name_plural = 'Miracle账单'



