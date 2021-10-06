from datetimepicker.widgets import DateTimePicker
from django.contrib import admin
from django.forms import forms  # 2021-02-27 admin添加导入功能，上传文件
from django.http import HttpResponse
from openpyxl import Workbook
from django.http import JsonResponse
from .models import Park, ParkManager,ParkLog
from simpleui.admin import AjaxAdmin
from import_export.admin import ImportExportModelAdmin



class ParkAdmin(ImportExportModelAdmin, AjaxAdmin):
    fieldsets = [(u'园区信息', {
        'fields': ['ParkName', 'Address']
    }), (u'街道信息', {
        'fields': ['Province', 'City','District','Street']
    }),(u'其他信息',{
        'fields' :['PM','Memo']
    })]
    search_fields = (
        'ParkName', 'Province', 'City', 'District', 'Street', 'Address', 'PM', 'RecordDate', 'UpdateDate', 'Memo')
    list_display = (
        'ParkName', 'Province', 'City', 'District', 'Street', 'Address', 'PM', 'RecordDate', 'UpdateDate', 'Memo',
        'pass_audit_str')
    list_filter = ('ParkName', 'City', 'District', 'Street', 'Address', 'PM', 'RecordDate', 'UpdateDate', 'Memo')
    list_per_page = 20
    autocomplete_fields = ['PM']


admin.site.register(Park, ParkAdmin)


# Register your models here.
class ParkManagerAdmin(ImportExportModelAdmin, AjaxAdmin):
    fields = ('PMName', 'Memo')
    search_fields = ('PMName', 'RecordDate', 'UpdateDate', 'Memo')
    list_display = ('PMName', 'RecordDate', 'UpdateDate', 'Memo')
    list_filter = ('PMName', 'RecordDate', 'UpdateDate', 'Memo')
    list_per_page = 20


admin.site.register(ParkManager, ParkManagerAdmin)


# Register your models here.
class ParkLogAdmin(ImportExportModelAdmin, AjaxAdmin):
    fields = ('Park', 'Title', 'Content', 'Memo')
    search_fields = ('Park', 'Title', 'Content', 'RecordDate', 'UpdateDate', 'Memo')
    list_display = ('Park', 'Title', 'Content', 'RecordDate', 'UpdateDate', 'Memo')
    list_filter = ('Park', 'Title', 'Content', 'RecordDate', 'UpdateDate', 'Memo')
    list_per_page = 20
    autocomplete_fields = ['Park']


admin.site.register(ParkLog, ParkLogAdmin)
