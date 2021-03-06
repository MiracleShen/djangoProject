from django.db import models

# Create your models here.
from django.db import models
from django.contrib import admin
from django.utils.html import format_html

# 关于号码的管理，主要在于当前号码是否可选、当前号码被谁占用了；当前号码开了几个并发（这个功能还需要EZUC+加以配合）
import crm.models


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
    STAR = (
        ('普通号', '普通号'),
        ('1星级', '1星级'),
        ('2星级', '2星级'),
        ('3星级', '3星级'),
        ('4星级', '4星级'),
        ('5星级', '5星级'),
    )
    Zip = models.CharField(max_length=4, default='021', verbose_name='区号')
    Number = models.CharField(max_length=8, verbose_name='固话号码')
    Stars = models.CharField(max_length=8, verbose_name='星级', default='普通号', choices=STAR)
    Operator = models.CharField(max_length=12, verbose_name='运营商', choices=OPERATORS)
    Status = models.CharField(max_length=8, verbose_name='状态', default='可选', choices=STATUSS)
    Organize = models.CharField(max_length=30, default=' ', verbose_name='客户名称')

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
        verbose_name_plural = '码号'


class MiracleOrders(models.Model):
    PBXTYPE = (
        ('免费版', '免费版'),
        ('查询版', '查询版'),
        ('管理版', '管理版'),
        ('本地部署版', '本地部署版'),

    )
    YESORNO = (
        ('无', '无'),
        ('有', '有'),
    )
    ORDERTYPE = (
        ('新增', '新增'),
        ('退订', '退订'),
    )
    CustomerName = models.ForeignKey('crm.Organization', on_delete=models.CASCADE, default='1', verbose_name='客户名称')
    OrderType = models.CharField(max_length=10, verbose_name='订单类型', default='新增', choices=ORDERTYPE)
    OrderDate = models.DateTimeField(verbose_name='生效时间')
    Number_0 = models.IntegerField(default=0, verbose_name='普通号码数')
    Number_1 = models.IntegerField(default=0, verbose_name='1星号码数')
    Number_2 = models.IntegerField(default=0, verbose_name='2星号码数')
    Number_3 = models.IntegerField(default=0, verbose_name='3星号码数')
    Number_4 = models.IntegerField(default=0, verbose_name='4星号码数')
    Number_5 = models.IntegerField(default=0, verbose_name='5星号码数')
    Line_Number = models.IntegerField(default=0, verbose_name='并发数')
    PBX_Type = models.CharField(max_length=10, verbose_name='交换机类型', default='免费版', choices=PBXTYPE)
    MCU_Type = models.CharField(max_length=10, verbose_name='多方通话许可', default='无', choices=YESORNO)
    API_Type = models.CharField(max_length=10, verbose_name='API许可', default='无', choices=YESORNO)
    APP_Number = models.IntegerField(default=0, verbose_name='APP许可数')
    SIP_Number = models.IntegerField(default=0, verbose_name='SIP许可数')
    Log_Number = models.IntegerField(default=0, verbose_name='录音许可数')
    CC_Number = models.IntegerField(default=0, verbose_name='轻客服许可数')
    HPR_Number = models.IntegerField(default=0, verbose_name='话机月租数量')  # 话机月租统一10元/月，WiFi话机，看长线

    class Meta:
        verbose_name_plural = 'Miracle订单'


# 话费账单，由EZUC+系统生成，每月月初手工录入到系统中
# 后期考虑系统自动从EZUC+抓取通话清单，系统自动计算生成月度账单到MiracleBill，用户也可以在系统中查询详单；实时的话单，还是要到服务器上去查看
class MiracleCredit(models.Model):
    Customer = models.ForeignKey('crm.Organization', null=True, on_delete=models.CASCADE, verbose_name='客户名称')
    Type= models.CharField(max_length=10, null=True,verbose_name='账户类型')
    Account = models.CharField(max_length=50, null=True,verbose_name='账户名称')
    Year = models.CharField(max_length=4, verbose_name='年份')
    Month = models.CharField(max_length=2, verbose_name='月份')
    Credit = models.FloatField(verbose_name='消费金额')
    RecordDate = models.DateTimeField(auto_now=True, verbose_name='记录时间')
    Memo = models.TextField(default='无', verbose_name='备注')
    class Meta:
        verbose_name_plural = 'Miracle话单'


class MiraclePBX(models.Model):
    Customer = models.ForeignKey('crm.Organization', default=1, on_delete=models.CASCADE, verbose_name='客户名称')
    Server = models.CharField(max_length=50, verbose_name='服务器')
    PBX = models.CharField(max_length=30, verbose_name='企业编号')
    RecordDate = models.DateTimeField(auto_now_add=True, verbose_name='记录时间')
    UpdateDate = models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')
    Memo = models.TextField(default='无', verbose_name='备注')
    class Meta:
        verbose_name_plural = '交换'


class MiracleDID(models.Model):
    Customer = models.ForeignKey('crm.Organization', default=1, on_delete=models.CASCADE, verbose_name='客户名称')
    Server = models.CharField(max_length=50, verbose_name='服务器')
    PBX = models.CharField(max_length=30, verbose_name='企业编号')
    DID = models.CharField(max_length=30, verbose_name='直线账户')
    RecordDate = models.DateTimeField(auto_now_add=True, verbose_name='记录时间')
    UpdateDate = models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')
    Memo = models.TextField(default='无', verbose_name='备注')
    class Meta:
        verbose_name_plural = '直线'


# 客户账单，目前由两部分生成，一部分是根据Miracle Order里的数据，每月自动计算生成月租费账单；另一部分是从EZUC+中获取每月话费账单，插入到Miracle Bill中。两者相加，就是用户当月应付的账单。
# 前期由慈俭运营人员每月月初手工生成账单发给客户，后期可以采用电子邮件的方式发送给客户的指定邮箱；或者短信、微信、电话的方式通知到用户的联系人，并告知对方付费。
class MiracleBill(models.Model):
    BILL_TYPE = (
        ('租金', '租金'),
        ('话费', '话费'),
    )
    BILL_STATUS = (
        ('已出账', '已出账'),
        ('已到账', '已到账'),
        ('已坏账', '已坏账'),
    )
    CustomerID = models.ForeignKey('crm.Organization', on_delete=models.CASCADE, verbose_name='客户名称')
    Year = models.CharField(max_length=4, verbose_name='年份')
    Month = models.CharField(max_length=2, verbose_name='月份')
    Bill_Cycle = models.CharField(max_length=2, verbose_name='计费周期')
    Bill_Type = models.CharField(choices=BILL_TYPE, default='租金', max_length=4, verbose_name='账单类型')
    Bill = models.FloatField(verbose_name='账单金额')
    Bill_Status = models.CharField(choices=BILL_STATUS, default='已出账', max_length=8, verbose_name='账单状态')
    RecordDate = models.DateTimeField(auto_now_add=True, verbose_name='记录时间')
    UpdateDate = models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')
    Memo = models.TextField(default='1', verbose_name='备注')

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

    def colored_Bill_Status(self):
        if self.Bill_Status == '已出账':
            color_code = 'blue'
        elif self.Bill_Status == '已到账':
            color_code = 'green'
        elif self.Bill_Status == '已坏账':
            color_code = 'red'
        else:
            color_code = 'black'
        return format_html(
            '<span style="color: {};">{}</span>',
            color_code,
            self.Bill_Status,
        )

    colored_Bill_Status.short_description = u"账单状态"

    class Meta:
        verbose_name_plural = 'Miracle账单'
