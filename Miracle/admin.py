# Register your models here.


from datetimepicker.widgets import DateTimePicker
from django.contrib import admin
from django.forms import forms  # 2021-02-27 admin添加导入功能，上传文件
from django.http import HttpResponse
from openpyxl import Workbook

from .models import MiracleNumber, MiracleOrders, MiracleCredit, MiracleBill
from simpleui.admin import AjaxAdmin
from import_export.admin import ImportExportModelAdmin
admin.AdminSite.site_header = 'MiracleOS系统'
admin.AdminSite.site_title = 'MiracleOS系统'



class MiracleNumberAdmin(ImportExportModelAdmin, AjaxAdmin):
    fields = ('Zip', 'Number', 'Stars','Operator', 'Status', 'Organize')
    search_fields = ('Zip', 'Number', 'Stars','Operator', 'Status', 'Organize')
    list_display = ('Zip', 'Number', 'Stars','Operator', 'colored_Status', 'Organize')
    list_filter = ('Zip', 'Operator', 'Stars','Status', 'Organize')
    list_per_page = 20
    # actions = ['export_as_excel']


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
    fields = ('CustomerID', 'Year', 'Month', 'Bill_Cycle', 'Bill_Type', 'Bill','Bill_Status','Memo')
    search_fields = ('CustomerID',)
    list_display = ('CustomerID', 'Year', 'Month', 'Bill_Cycle', 'colored_Bill_Type', 'Bill', 'colored_Bill_Status', 'RecordDate','UpdateDate', 'Memo')
    list_per_page = 20
    list_filter = ('Year', 'Month', 'Bill_Cycle', 'Bill_Type','Bill_Status')
    ordering = ['-UpdateDate']
    autocomplete_fields = ['CustomerID']


admin.site.register(MiracleBill, MiracleBillAdmin)
