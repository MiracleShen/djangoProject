from django.contrib import admin
from Miracle.admin import ExportExcelMixin
from .models import *



# Register your models here.


# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    fields = ('tasktype', 'name', 'content', 'status','Owner')
    search_fields = ('tasktype', 'name', 'content', 'status','Owner', 'Creator')
    list_display = ('tasktype', 'name', 'short_content', 'colored_status', 'createdtime', 'updatedtime','Owner', 'Creator')
    list_filter = ('tasktype', 'status', 'Owner', 'createdtime', 'updatedtime')
    list_per_page = 15
    actions = ['export_as_excel']
    ordering = ['-updatedtime']

    def get_queryset(self, request):  # 重写get_queryset
        qs = super(TaskAdmin, self).get_queryset(request)
        if request.user.is_superuser:  # 判断如果是超级管理员返回所有信息
            return qs
        else:
            return qs.filter(Owner=request.user.last_name + request.user.first_name)  # User为当前关联的用户，如果是普通管理员只能看自己

    def save_model(self, request, obj, form, change):
        if not change:
            # the object is being created, so set the user
            obj.Owner = request.user.last_name + request.user.first_name
            obj.Creator = request.user.last_name + request.user.first_name
        obj.save()


admin.site.register(Task, TaskAdmin)


