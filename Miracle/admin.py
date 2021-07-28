# Register your models here.


from datetimepicker.widgets import DateTimePicker
from django.contrib import admin
from django.forms import forms  # 2021-02-27 admin添加导入功能，上传文件
from django.http import HttpResponse
from openpyxl import Workbook
from django.http import JsonResponse
from .models import MiracleNumber, MiracleOrders, MiracleCredit, MiracleBill
from simpleui.admin import AjaxAdmin
from import_export.admin import ImportExportModelAdmin

admin.AdminSite.site_header = 'MiracleOS系统'
admin.AdminSite.site_title = 'MiracleOS系统'


class MiracleNumberAdmin(ImportExportModelAdmin, AjaxAdmin):
    fields = ('Zip', 'Number', 'Stars', 'Operator', 'Status', 'Organize')
    search_fields = ('Zip', 'Number', 'Stars', 'Operator', 'Status', 'Organize')
    list_display = ('Zip', 'Number', 'Stars', 'Operator', 'colored_Status', 'Organize')
    list_filter = ('Zip', 'Operator', 'Stars', 'Status', 'Organize')
    list_per_page = 20
    actions = ['NumberStatus', 'NumberReport','NumberOrganizeReport']

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
        'CustomerName', 'OrderDate', 'Number_0', 'Number_1', 'Number_2', 'Number_3', 'Number_4', 'Number_5',
        'Line_Number',
        'PBX_Type', 'MCU_Type', 'API_Type', 'APP_Number', 'SIP_Number', 'Log_Number', 'CC_Number', 'HPR_Number')
    search_fields = ('CustomerName', 'OrderDate', 'PBX_Type', 'MCU_Type', 'API_Type')
    list_display = (
        'CustomerName', 'OrderDate', 'Number_0', 'Number_1', 'Line_Number', 'PBX_Type', 'MCU_Type', 'API_Type',
        'APP_Number', 'SIP_Number', 'Log_Number', 'CC_Number', 'HPR_Number')
    list_filter = ('OrderDate',)
    date_hierarchy = 'OrderDate'
    formfield_overrides = {
        MiracleOrders.OrderDate: {'widget': DateTimePicker},
    }
    show_full_result_count = True
    list_per_page = 10
    actions = ['export_as_excel']


admin.site.register(MiracleOrders, MiracleOrdersAdmin)


class MiracleCreditAdmin(admin.ModelAdmin):
    fields = ('CustomerID', 'Year', 'Month', 'Credit')
    search_fields = ('CustomerID',)
    list_display = ('CustomerID', 'Year', 'Month', 'Credit', 'RecordDate')
    list_per_page = 10


admin.site.register(MiracleCredit, MiracleCreditAdmin)


class MiracleBillAdmin(admin.ModelAdmin):
    fields = ('CustomerID', 'Year', 'Month', 'Bill_Cycle', 'Bill_Type', 'Bill', 'Bill_Status', 'Memo')
    search_fields = ('CustomerID',)
    list_display = (
    'CustomerID', 'Year', 'Month', 'Bill_Cycle', 'colored_Bill_Type', 'Bill', 'colored_Bill_Status', 'RecordDate',
    'UpdateDate', 'Memo')
    list_per_page = 20
    list_filter = ('Year', 'Month', 'Bill_Cycle', 'Bill_Type', 'Bill_Status')
    ordering = ['-UpdateDate']
    autocomplete_fields = ['CustomerID']


admin.site.register(MiracleBill, MiracleBillAdmin)
