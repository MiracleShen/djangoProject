from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import MiracleNumber,MiracleOrders,MiracleCredit
from datetimepicker.widgets import DateTimePicker
admin.AdminSite.site_header = 'Miracle电话运营管理系统'
admin.AdminSite.site_title = 'Miracle电话运营管理系统'

class MiracleNumberAdmin(admin.ModelAdmin):
    fields = ('Zip','Number','Operator','Status')
    search_fields = ('Zip','Number','Operator','Status')
    list_display = ('Zip','Number','Operator','colored_Status')
admin.site.register(MiracleNumber,MiracleNumberAdmin)

class MiracleOrdersAdmin(admin.ModelAdmin):
    fields = ('CustomerName','OrderDate','Number_0','Number_1','Number_2','Number_3','Number_4','Number_5','Line_Number','PBX_Type','MCU_Type','API_Type','APP_Number','SIP_Number','Log_Number','CC_Number','HPR_Number')
    search_fields = ('CustomerName','OrderDate','PBX_Type','MCU_Type','API_Type')
    list_display = ('CustomerName','OrderDate','Number_0','Number_1','Line_Number','PBX_Type','MCU_Type','API_Type','APP_Number','SIP_Number','Log_Number','CC_Number','HPR_Number')
    list_filter = ('OrderDate',)
    date_hierarchy = 'OrderDate'
    formfield_overrides = {
        MiracleOrders.OrderDate: {'widget': DateTimePicker},
    }
    show_full_result_count=True
admin.site.register(MiracleOrders,MiracleOrdersAdmin)

class MiracleCreditAdmin(admin.ModelAdmin):
    fields = ('CustomerName','Year','Month','Credit')
    search_fields = ('CustomerName',)
    list_display = ('CustomerName','Year','Month','Credit','RecordDate')
admin.site.register(MiracleCredit,MiracleCreditAdmin)
