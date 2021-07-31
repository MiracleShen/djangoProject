from django.contrib import admin
from .models import *

from simpleui.admin import AjaxAdmin
from import_export.admin import ImportExportModelAdmin
from django.http import JsonResponse
# Register your models here.


# Register your models here.
class TaskAdmin(ImportExportModelAdmin,AjaxAdmin):
    fields = ('tasktype', 'name', 'content', 'status','Owner')
    search_fields = ('tasktype', 'name', 'content', 'status','Owner', 'Creator')
    list_display = ('tasktype', 'name', 'short_content', 'colored_status', 'createdtime', 'updatedtime','Owner', 'Creator')
    list_filter = ('tasktype', 'status', 'Owner', 'createdtime', 'updatedtime')
    list_per_page = 15
    ordering = ['-updatedtime']
    actions = ( 'Task_assign',)
    def Task_assign(self, request, queryset):

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
            # print('我是参数'+post['type'])
            if request.user.is_superuser:
                for qs in queryset:
                    self.model.objects.filter(id=qs.id).update(Owner=post['type'])
                    # print(str(qs.id)+'我被选中了'+qs.Owner)
                return JsonResponse(data={
                    'status': 'success',
                    'msg': '处理成功！'
                })
            else:
                return JsonResponse(data={
                    'status': 'error',
                    'msg': '您没有权限，请找管理员分配数据'
                })

    Task_assign.short_description = '分配任务'
    Task_assign.type = 'success'
    Task_assign.icon = 'el-icon-s-promotion'
    Task_assign.layer = {
        'title': '批量分配数据',
        'tips': '勾选多条数据，批量分配数据给执行人',
        'confirm_button': '确认提交',
        'cancel_button': '取消',
        'width': '40%',
        'labelWidth': "80px",
        'params': [
            {
                'type': 'radio',
                'key': 'type',
                'label': '执行人',
                'width': '500px',
                'size': 'small',
                'value': '沈承永',
                'options': [{
                    'key': '沈承永',
                    'label': '沈承永'
                }, {
                    'key': '耿萌萌',
                    'label': '耿萌萌'
                }, {
                    'key': '王忠盟',
                    'label': '王忠盟'
                },]
            }, ]
    }

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


