from django.contrib import admin

# Register your models here.

from openpyxl import Workbook
from django.contrib import admin
from .models import MiracleNumber, MiracleOrders, MiracleCredit
from datetimepicker.widgets import DateTimePicker
from django.forms import forms #2021-02-27 admin添加导入功能，上传文件
from django.http import HttpResponse

admin.AdminSite.site_header = 'Miracle电话运营管理系统'
admin.AdminSite.site_title = 'Miracle电话运营管理系统'


class ExportExcelMixin(object):
  def export_as_excel(self, request, queryset):
    meta = self.model._meta
    field_names = [field.name for field in meta.fields]
    response = HttpResponse(content_type='application/msexcel')
    response['Content-Disposition'] = f'attachment; filename={meta}.xlsx'
    wb = Workbook()
    ws = wb.active
    ws.append(field_names)
    for obj in queryset:
      for field in field_names:
        data = [f'{getattr(obj, field)}' for field in field_names]
      row = ws.append(data)
    wb.save(response)
    return response
  export_as_excel.short_description = '导出Excel'


class ExcelImportForm(forms.Form):
    excel_file = forms.FileField()

class MiracleNumberAdmin(admin.ModelAdmin,ExportExcelMixin):
    fields = ('Zip', 'Number', 'Operator', 'Status','Organize')
    search_fields = ('Zip', 'Number', 'Operator', 'Status','Organize')
    list_display = ('Zip', 'Number', 'Operator', 'colored_Status','Organize')
    list_filter = ('Zip', 'Operator', 'Status','Organize')
    list_per_page = 10
    actions = ['export_as_excel']

admin.site.register(MiracleNumber, MiracleNumberAdmin)


class MiracleOrdersAdmin(admin.ModelAdmin,ExportExcelMixin):
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
    list_per_page =10
    actions = ['export_as_excel']

admin.site.register(MiracleOrders, MiracleOrdersAdmin)


class MiracleCreditAdmin(admin.ModelAdmin):
    fields = ('CustomerName', 'Year', 'Month', 'Credit')
    search_fields = ('CustomerName',)
    list_display = ('CustomerName', 'Year', 'Month', 'Credit', 'RecordDate')
    list_per_page = 10


admin.site.register(MiracleCredit, MiracleCreditAdmin)



