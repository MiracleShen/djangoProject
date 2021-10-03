

from datetimepicker.widgets import DateTimePicker
from django.contrib import admin
from django.forms import forms  # 2021-02-27 admin添加导入功能，上传文件
from django.http import HttpResponse
from openpyxl import Workbook
from django.http import JsonResponse
from .models import Card,Device,CloudNet,Ticket
from simpleui.admin import AjaxAdmin
from import_export.admin import ImportExportModelAdmin
# Register your models here.
class CardAdmin(ImportExportModelAdmin, AjaxAdmin):
    fields = ('CardNumber','Device','Operator','Memo')
    search_fields = ('CardNumber','Device__Mac','Device__SN','Operator','RecordDate','UpdateDate','Memo')
    list_display = ('CardNumber','Device','Operator','RecordDate','UpdateDate','Memo')
    list_filter = ('CardNumber','Device','Operator','RecordDate','UpdateDate','Memo')
    list_per_page = 20
    autocomplete_fields = ['Device']
admin.site.register(Card, CardAdmin)

class DeviceAdmin(ImportExportModelAdmin, AjaxAdmin):
    fields = ('Mac','SN','Type','Memo')
    search_fields = ('Mac','SN','Type','RecordDate','UpdateDate','Memo')
    list_display = ('Mac','SN','Type','RecordDate','UpdateDate','Memo')
    list_filter = ('Mac','SN','Type','RecordDate','UpdateDate','Memo')
    list_per_page = 20

admin.site.register(Device, DeviceAdmin)

class CloudNetAdmin(ImportExportModelAdmin, AjaxAdmin):
    fields = ('Organize','Device','StartDate','EndDate','Memo')
    search_fields = ('Organize__OrganizeName','Device__Mac','StartDate','EndDate','Memo')
    list_display = ('Organize','Device','StartDate','EndDate','Memo')
    list_filter = ('Organize','Device','StartDate','EndDate','Memo')
    list_per_page = 20
    autocomplete_fields = ['Organize','Device']
admin.site.register(CloudNet, CloudNetAdmin)

class TicketAdmin(ImportExportModelAdmin, AjaxAdmin):
    fields = ('Organize','Title','Type','Content','Worker','DateTime','Memo')
    search_fields = ('Organize__OrganizeName','Title','Type','Content','Worker','DateTime','Memo')
    list_display = ('Organize','Title','Type','Content','Worker','DateTime','Memo')
    list_filter = ('Organize','Title','Type','Content','Worker','DateTime','Memo')
    list_per_page = 20
    autocomplete_fields = ['Organize']
admin.site.register(Ticket, TicketAdmin)