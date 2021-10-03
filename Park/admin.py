from datetimepicker.widgets import DateTimePicker
from django.contrib import admin
from django.forms import forms  # 2021-02-27 admin添加导入功能，上传文件
from django.http import HttpResponse
from openpyxl import Workbook
from django.http import JsonResponse
from .models import Park,ParkManager,Street,ParkLog
from simpleui.admin import AjaxAdmin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class StreetAdmin(ImportExportModelAdmin, AjaxAdmin):
    fields = ('StreetName','Memo')
    search_fields = ('StreetName','RecordDate','UpdateDate','Memo')
    list_display = ('StreetName','RecordDate','UpdateDate','Memo')
    list_filter = ('StreetName','RecordDate','UpdateDate','Memo')
    list_per_page = 20
admin.site.register(Street, StreetAdmin)
class ParkAdmin(ImportExportModelAdmin, AjaxAdmin):
    fields = ('XY','Street','No','ParkName','PM','Memo')
    search_fields = ('XY','Street','No','ParkName','PM','RecordDate','UpdateDate','Memo')
    list_display = ('XY','Street','No','ParkName','PM','RecordDate','UpdateDate','Memo')
    list_filter = ('XY','Street','No','ParkName','PM','RecordDate','UpdateDate','Memo')
    list_per_page = 20
    autocomplete_fields = ['Street','PM']
admin.site.register(Park, ParkAdmin)
# Register your models here.
class ParkManagerAdmin(ImportExportModelAdmin, AjaxAdmin):
    fields = ('PMName','Memo')
    search_fields = ('PMName','RecordDate','UpdateDate','Memo')
    list_display = ('PMName','RecordDate','UpdateDate','Memo')
    list_filter = ('PMName','RecordDate','UpdateDate','Memo')
    list_per_page = 20
admin.site.register(ParkManager, ParkManagerAdmin)
# Register your models here.
class ParkLogAdmin(ImportExportModelAdmin, AjaxAdmin):
    fields = ('Park','Title','Content','Memo')
    search_fields = ('Park','Title','Content','RecordDate','UpdateDate','Memo')
    list_display = ('Park','Title','Content','RecordDate','UpdateDate','Memo')
    list_filter = ('Park','Title','Content','RecordDate','UpdateDate','Memo')
    list_per_page = 20
    autocomplete_fields = ['Park']
admin.site.register(ParkLog, ParkLogAdmin)