from datetimepicker.widgets import DateTimePicker
from django.contrib import admin
from django.forms import forms  # 2021-02-27 admin添加导入功能，上传文件
from django.http import HttpResponse
from openpyxl import Workbook
from django.http import JsonResponse
from .models import Park, ParkManager, ParkLog
from simpleui.admin import AjaxAdmin
from import_export.admin import ImportExportModelAdmin
import requests, json


# class ParkAdmin(ImportExportModelAdmin, AjaxAdmin):
class ParkAdmin(admin.ModelAdmin):
    fieldsets = [(u'园区信息', {
        'fields': ['ParkName', 'Address']
    }), (u'其他信息', {
        'fields': ['PM', 'Memo']
    })]
    search_fields = (
        'ParkName', 'Province', 'City', 'District', 'Town', 'Address', 'PM', 'RecordDate', 'UpdateDate', 'Memo')
    list_display = (
        'ParkName', 'Province', 'City', 'District', 'Town', 'Address', 'PM', 'RecordDate', 'UpdateDate', 'Memo',
        # 'pass_audit_str'
    )
    list_filter = ('ParkName', 'City', 'District', 'Town', 'Address', 'PM', 'RecordDate', 'UpdateDate', 'Memo')
    list_per_page = 20
    autocomplete_fields = ['PM']

    def save_model(self, request, obj, form, change):
        ADDRESS = obj.Address
        print(ADDRESS)
        # 根据园区名称获得坐标
        URL2 = 'https://api.map.baidu.com/geocoding/v3/'
        params2 = {
            "ak": 'Xmjf4HD2kly5zqZybYhmZV9RW7fx7ass',
            "output": 'json',
            "address": ADDRESS,
            "ret_coordtype": 'bd09II',
        }
        res2 = requests.get(url=URL2, params=params2)
        res22 = json.loads(res2.text)
        res23 = str(res22['result']['location']['lat']) + ',' + str(res22['result']['location']['lng'])
        # 根据坐标获得所在的国家、省份、城市、区县、乡镇、街道
        URL3 = 'https://api.map.baidu.com/reverse_geocoding/v3/'
        ####测试行级按钮获得六级地址
        params3 = {
            "ak": 'Xmjf4HD2kly5zqZybYhmZV9RW7fx7ass',
            "output": 'json',
            "coordtype": 'bd09II',
            "ret_coordtype": 'bd09II',
            "extensions_town": "true",
            "extensions_road": "true",
            "location": res23,
            "sub_admin": 3
        }
        res3 = requests.get(url=URL3, params=params3)
        print(res3.text)
        res33 = json.loads(res3.text)['result']
        #####测试行级按钮获取六级地址
        add = json.loads(res3.text)['result']
        add1 = add['addressComponent']['province'] + add['addressComponent']['city'] + add['addressComponent'][
            'district'] + add['addressComponent']['town']
        res33 = res23

        obj.Province = add['addressComponent']['province']
        obj.City = add['addressComponent']['city']
        obj.District = add['addressComponent']['district']
        obj.Town = add['addressComponent']['town']
        print(obj.Province)
        super().save_model(request, obj, form, change)


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
