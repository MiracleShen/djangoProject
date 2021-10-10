# Register your models here.


from datetimepicker.widgets import DateTimePicker
from django.contrib import admin
from django.forms import forms  # 2021-02-27 admin添加导入功能，上传文件
from django.http import HttpResponse
from openpyxl import Workbook
from django.http import JsonResponse
from .models import MiracleNumber, MiracleOrders, MiracleCredit, MiracleBill, MiraclePBX, MiracleDID
from simpleui.admin import AjaxAdmin
from import_export.admin import ImportExportModelAdmin
from django.contrib import messages
admin.AdminSite.site_header = 'MiracleOS系统'
admin.AdminSite.site_title = 'MiracleOS系统'


class MiracleNumberAdmin(ImportExportModelAdmin, AjaxAdmin):
    fields = ('Zip', 'Number', 'Stars', 'Operator', 'Status', 'Organize')
    search_fields = ('Zip', 'Number', 'Stars', 'Operator', 'Status', 'Organize')
    list_display = ('Zip', 'Number', 'Stars', 'Operator', 'colored_Status', 'Organize')
    list_filter = ('Zip', 'Operator', 'Stars', 'Status', 'Organize')
    list_per_page = 20
    actions = ['NumberStatus', 'NumberReport', 'NumberOrganizeReport']

    def NumberReport(self, request, queryset):
        pass

    NumberReport.short_description = '号码状态报表'
    NumberReport.icon = 'fas fa-audio-description'
    NumberReport.type = 'success'
    NumberReport.action_type = 1
    NumberReport.action_url = '/crm/NumberReport/'

    def NumberOrganizeReport(self, request, queryset):
        pass

    NumberOrganizeReport.short_description = '客户号码报表'
    NumberOrganizeReport.icon = 'fas fa-audio-description'
    NumberOrganizeReport.type = 'success'
    NumberOrganizeReport.action_type = 1
    NumberOrganizeReport.action_url = '/crm/NumberOrganizeReport/'

    def NumberStatus(self, request, queryset):
        post = request.POST
        # 这里获取到数据后，可以做些业务处理
        # post中的_action 是方法名
        # post中 _selected 是选中的数据，逗号分割
        if not post.get('_selected'):
            return JsonResponse(data={
                'status': 'error',
                'msg': '请选择数据'
            })
        else:
            for qs in queryset:
                self.model.objects.filter(id=qs.id).update(Organize=post['Memo'], Status=post['Status'])
                # print(str(qs.id)+'我被选中了'+qs.Owner)
            return JsonResponse(data={
                'status': 'success',
                'msg': '处理成功！'
            })

    NumberStatus.short_description = '更改号码状态'
    NumberStatus.type = 'success'
    NumberStatus.icon = 'el-icon-s-promotion'

    # 指定一个输入参数，应该是一个数组

    # 指定为弹出层，这个参数最关键
    NumberStatus.layer = {
        'title': '沟通内容',
        'tips': '填写沟通内容',
        'confirm_button': '确认提交',
        'cancel_button': '取消',
        'width': '40%',
        'labelWidth': "80px",
        'params': [
            {
                'type': 'radio',
                'key': 'Status',
                'label': '沟通结果',
                'width': '500px',
                'size': 'large',
                'value': '可选',
                'required': True,
                'options': [
                    {
                        'key': '可选',
                        'label': '可选'
                    },
                    {
                        'key': '锁定',
                        'label': '锁定'
                    },
                    {
                        'key': '已售',
                        'label': '已售'
                    },
                ]
            }, {
                'type': 'textarea',
                'key': 'Memo',
                'label': '公司',
                'width': '500px',
                'size': 'large',
                'value': '无',
                'required': True
            }]
    }


admin.site.register(MiracleNumber, MiracleNumberAdmin)


class MiracleOrdersAdmin(ImportExportModelAdmin, AjaxAdmin):
    fields = (
        'CustomerName', 'OrderType', 'OrderDate', 'Number_0', 'Number_1', 'Number_2', 'Number_3', 'Number_4',
        'Number_5',
        'Line_Number',
        'PBX_Type', 'MCU_Type', 'API_Type', 'APP_Number', 'SIP_Number', 'Log_Number', 'CC_Number', 'HPR_Number')
    search_fields = ('CustomerName', 'OrderType', 'OrderDate', 'PBX_Type', 'MCU_Type', 'API_Type')
    list_display = (
        'CustomerName', 'OrderType', 'OrderDate', 'Number_0', 'Number_1', 'Line_Number', 'PBX_Type', 'MCU_Type',
        'API_Type',
        'APP_Number', 'SIP_Number', 'Log_Number', 'CC_Number', 'HPR_Number')
    list_filter = ('OrderDate',)
    date_hierarchy = 'OrderDate'
    formfield_overrides = {
        MiracleOrders.OrderDate: {'widget': DateTimePicker},
    }
    show_full_result_count = True
    list_per_page = 10
    actions = ['export_as_excel','NumberCount','PBXCount','PhoneCount','LogCount','CCCount','HPRCount']
    def PhoneCount(self,request,queryset):
       NUM=0
       for qs in queryset:
           NUM = NUM+qs.APP_Number+qs.SIP_Number
       return messages.success(request,'选中的订单一共订购了'+str(NUM)+'个电话账户')
    def LogCount(self,request,queryset):
       NUM=0
       for qs in queryset:
           NUM = NUM+qs.Log_Number
       return messages.success(request,'选中的订单一共订购了'+str(NUM)+'个录音账户')
    def CCCount(self,request,queryset):
       NUM=0
       for qs in queryset:
           NUM = NUM+qs.CC_Number
       return messages.success(request,'选中的订单一共订购了'+str(NUM)+'个客服账户')
    def HPRCount(self,request,queryset):
       NUM=0
       for qs in queryset:
           NUM = NUM+qs.HPR_Number
       return messages.success(request,'选中的订单一共订购了'+str(NUM)+'个话机租赁')
    def NumberCount(self,request,queryset):
       NUM=0
       for qs in queryset:
           NUM = NUM+qs.Number_0+qs.Number_1+qs.Number_2+qs.Number_3+qs.Number_4+qs.Number_5
       return messages.success(request,'选中的订单一共订购了'+str(NUM)+'个电话号码')
    def PBXCount(self,request,queryset):
       A=0
       B=0
       C=0
       for qs in queryset:
           if qs.PBX_Type=='免费版':
               A = A+1
           elif qs.PBX_Type=='管理版':
               B = B+1
           elif qs.PBX_Type=='本地部署版':
               C = C+1

       return messages.success(request,'免费版：'+str(A)+'个；'+'管理版：'+str(B)+'个；'+'本地部署版：'+str(C)+'个。')

admin.site.register(MiracleOrders, MiracleOrdersAdmin)


class MiracleCreditAdmin(admin.ModelAdmin):
    fields = ('Customer','Type','Account', 'Year', 'Month', 'Credit','Memo')
    search_fields = ('Customer','Type','Account','Memo')
    list_display = ('Customer','Type','Account', 'Year', 'Month', 'Credit', 'RecordDate','Memo')
    list_per_page = 20


admin.site.register(MiracleCredit, MiracleCreditAdmin)


class MiracleBillAdmin(admin.ModelAdmin):
    fields = ('CustomerID', 'Year', 'Month', 'Bill_Cycle', 'Bill_Type', 'Bill', 'Bill_Status', 'Memo')
    search_fields = ('CustomerID__OrganizeName',)
    list_display = (
        'CustomerID', 'Year', 'Month', 'Bill_Cycle', 'colored_Bill_Type', 'Bill', 'colored_Bill_Status', 'RecordDate',
        'UpdateDate', 'Memo')
    list_per_page = 20
    list_filter = ('Year', 'Month', 'Bill_Cycle', 'Bill_Type', 'Bill_Status')
    ordering = ['-UpdateDate']
    autocomplete_fields = ['CustomerID']


admin.site.register(MiracleBill, MiracleBillAdmin)


class MiraclePBXAdmin(ImportExportModelAdmin, AjaxAdmin):
    fields = ('Customer', 'Server', 'PBX', 'Memo')
    search_fields = ('Customer__OrganizeName', 'Server', 'PBX','Memo')
    list_display = ('Customer', 'Server', 'PBX', 'RecordDate', 'UpdateDate', 'Memo')
    list_per_page = 20
    autocomplete_fields = ['Customer']


admin.site.register(MiraclePBX, MiraclePBXAdmin)


class MiracleDIDAdmin(ImportExportModelAdmin, AjaxAdmin):
    fields = ('Customer', 'Server', 'PBX', 'DID', 'Memo')
    search_fields = ('Customer__OrganizeName', 'Server', 'PBX', 'DID')
    list_display = ('Customer', 'Server', 'PBX', 'DID', 'RecordDate', 'UpdateDate', 'Memo')
    list_per_page = 20
    autocomplete_fields = ['Customer']


admin.site.register(MiracleDID, MiracleDIDAdmin)
