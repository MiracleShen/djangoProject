from django.contrib import admin
from .models import *
from django.http import JsonResponse
from simpleui.admin import AjaxAdmin
from import_export.admin import ImportExportModelAdmin


class ContactHistoryInline(admin.StackedInline):
    model = ContactHistory
    fields = ('Contact', 'ContactType', 'Memo', 'Creator', 'ContactDateTime')
    extra = 0
    raw_id_fields = ('Contact',)
    readonly_fields = ['ContactType', 'Memo', 'Creator', 'ContactDateTime']
    can_delete = False


class ContactHistoryAdmin(admin.ModelAdmin):
    fields = ('Contact', 'ContactType', 'Memo')
    search_fields = ('Contact__Name', 'Contact__Organize__OrganizeName', 'ContactType', 'Memo', 'Creator')
    list_display = ('Contact', 'colored_ContactType', 'Memo', 'ContactDateTime', 'Creator')
    list_filter = ('Contact', 'ContactType', 'Memo', 'ContactDateTime', 'Creator')
    autocomplete_fields = ['Contact']

    def get_queryset(self, request):  # 重写get_queryset
        qs = super(ContactHistoryAdmin, self).get_queryset(request)
        if request.user.is_superuser:  # 判断如果是超级管理员返回所有信息
            return qs
        else:
            return qs.filter(Creator=request.user.last_name + request.user.first_name)  # User为当前关联的用户，如果是普通管理员只能看自己

    def save_model(self, request, obj, form, change):
        if not change:
            # the object is being created, so set the user
            obj.Creator = request.user.last_name + request.user.first_name
        obj.save()


admin.site.register(ContactHistory, ContactHistoryAdmin)


class ContactsAdmin(admin.ModelAdmin):
    search_fields = ('Organize__OrganizeName', 'Name', 'Mobile', 'Email', 'Memo')
    list_display = ('Name', 'Organize', 'Mobile', 'Email', 'Memo')
    list_filter = ('Organize', 'Name', 'Mobile', 'Email', 'Memo')
    autocomplete_fields = ['Organize']
    fieldsets = [
        ('基础信息', {'fields': ('Organize', 'Name')}),
        ('联系信息', {'fields': ('Mobile', 'Email')}),
        ('备注信息', {'fields': ('Memo',)})]
    inlines = [
        ContactHistoryInline,
    ]


admin.site.register(Contacts, ContactsAdmin)
class ContactsInline(admin.StackedInline):
    model = Contacts
    fields = ('Name', 'Organize', 'Mobile', 'Email', 'Memo')
    extra = 0
    # readonly_fields = ['Name', 'Organize', 'Mobile', 'Email', 'Memo']
    can_delete = False

class OrganizationAdmin(ImportExportModelAdmin):
    fields = ('OrganizeName', 'OrganizeID', 'Memo')
    search_fields = ('OrganizeName', 'OrganizeID', 'Memo')
    list_display = ('OrganizeName', 'OrganizeID', 'Memo')
    list_filter = ('OrganizeName', 'OrganizeID', 'Memo')
    inlines = [
        ContactsInline,
    ]


admin.site.register(Organization, OrganizationAdmin)


class OblistAdmin(ImportExportModelAdmin, AjaxAdmin):
    fields = ('Campaign', 'Name', 'Phone1', 'Phone2', 'Status', 'Memo', 'Owner')
    search_fields = ('Campaign', 'Name', 'Phone1', 'Phone2', 'Status', 'Memo', 'Owner')
    list_display = (
    'Campaign', 'Name', 'Phone1', 'Phone2', 'Status', 'colored_Status', 'short_content', 'Owner', 'makecall')
    list_filter = ('Campaign', 'Name', 'Phone1', 'Phone2', 'Status', 'Memo', 'Owner')
    # list_editable = ('Status', 'Owner')
    actions = ('CallDetail', 'layer_input', 'Status_report')

    def CallDetail(self, request, queryset):
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
                self.model.objects.filter(id=qs.id).update(Memo=post['Memo'], Status=post['Status'])
                # print(str(qs.id)+'我被选中了'+qs.Owner)
            return JsonResponse(data={
                'status': 'success',
                'msg': '处理成功！'
            })

    CallDetail.short_description = '添加沟通结果'
    CallDetail.type = 'success'
    CallDetail.icon = 'el-icon-s-promotion'

    # 指定一个输入参数，应该是一个数组

    # 指定为弹出层，这个参数最关键
    CallDetail.layer = {
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
                'value': '有需求',
                'required': True,
                'options': [
                    {
                        'key': '有需求',
                        'label': '有需求'
                    },
                    {
                        'key': '有意向',
                        'label': '有意向'
                    },
                    {
                        'key': '再联系',
                        'label': '再联系'
                    },
                    {
                        'key': '拒绝沟通',
                        'label': '拒绝沟通'
                    },
                    {
                        'key': '未接通',
                        'label': '未接通'
                    },
                ]
            }, {
                'type': 'textarea',
                'key': 'Memo',
                'label': '沟通内容',
                'width': '500px',
                'size': 'large',
                'value': '',
                'required': True
            }]
    }

    def Status_report(self, request, queryset):
        pass

    Status_report.short_description = '数据报表'
    Status_report.icon = 'fas fa-audio-description'
    Status_report.type = 'success'
    Status_report.action_type = 1
    Status_report.action_url = '/crm/'

    def layer_input(self, request, queryset):

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

    layer_input.short_description = '分配数据'
    layer_input.type = 'success'
    layer_input.icon = 'el-icon-s-promotion'

    # 指定一个输入参数，应该是一个数组

    # 指定为弹出层，这个参数最关键
    layer_input.layer = {
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
                    'key': '王志杰',
                    'label': '王志杰'
                },
                ]
            }, ]
    }

    def makecall(self, obj):
        # html = '<a target="blank" href="/makecall/?destNumber='
        # html = html + obj.Phone1
        # html = html +'">拨打<a/>'
        html = '<button type="success" icon="el-icon-phone" onclick="makecall('
        html = html + obj.Phone1
        html = html + ')">拨打1</button>'
        if obj.Phone2:
            # print('我有老二：' + obj.Phone2)
            html = html + '<button type="success" icon="el-icon-phone" onclick="makecall('
            html = html + obj.Phone2
            html = html + ')">拨打2</button>'
        return format_html(html)

    makecall.short_description = '功能按钮'

    def get_queryset(self, request):  # 重写get_queryset
        qs = super(OblistAdmin, self).get_queryset(request)
        if request.user.is_superuser:  # 判断如果是超级管理员返回所有信息
            return qs
        else:
            return qs.filter(Owner=request.user.last_name + request.user.first_name)  # User为当前关联的用户，如果是普通管理员只能看自己

    class Media:
        js = ('js/call.js',)


admin.site.register(Oblist, OblistAdmin)
