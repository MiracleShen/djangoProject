from django.contrib import admin
from .models import *
from django.http import JsonResponse
from simpleui.admin import AjaxAdmin
from import_export.admin import ImportExportModelAdmin
from Park.admin import ParkAdmin
from Park.models import Park

# 1、 联系历史模块

# 1.1、 联系历史记录管理

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


# 1.2、 注册联系历史模块
admin.site.register(ContactHistory, ContactHistoryAdmin)


# 2、联系人
# 2.1、 联系人内联的联系历史记录

class ContactHistoryInline(admin.TabularInline):
    model = ContactHistory
    fields = ('Contact', 'ContactType', 'Memo', 'Creator', 'ContactDateTime')
    extra = 0
    raw_id_fields = ('Contact',)
    readonly_fields = ['ContactType', 'Memo', 'Creator', 'ContactDateTime']
    can_delete = False


# 2.2、 联系人管理
class ContactsAdmin(admin.ModelAdmin):
    search_fields = ('Organize__OrganizeName', 'Name', 'Mobile', 'Email', 'Memo')
    list_display = ('Name', 'Organize', 'Mobile', 'Email', 'Memo', 'AddContactLog')
    list_filter = ('Organize', 'Name', 'Mobile', 'Email', 'Memo')
    autocomplete_fields = ['Organize']
    fieldsets = [
        ('基础信息', {'fields': ('Organize', 'Name')}),
        ('联系信息', {'fields': ('Mobile', 'Email')}),
        ('备注信息', {'fields': ('Memo',)})]
    inlines = [
        ContactHistoryInline,
    ]
    # Tabular内联模式把多余的Original显示去除
    class Media:
        css = {"all": ("css/HideAdminOriginal.css",)}

# 2.3、 注册联系人
admin.site.register(Contacts, ContactsAdmin)

# 3、 组织
# 3.1、组织内联联系人
class ContactsInline(admin.TabularInline):
    model = Contacts
    fields = ('Name', 'Organize', 'Mobile', 'Email', 'Memo')
    extra = 0
    readonly_fields = ['Name', 'Organize', 'Mobile', 'Email', 'Memo']
    can_delete = False

# 3.2、组织管理

class OrganizationAdmin(ImportExportModelAdmin, AjaxAdmin):
    fieldsets = [(u'公司信息', {
        'fields': ['OrganizeName', 'OrganizeID']
    }), (u'园区信息', {
        'fields': ['Park']
    }), (u'其他信息', {
        'fields': ['Memo']
    })]
    search_fields = ('Park__ParkName','OrganizeName', 'OrganizeID', 'Memo')
    list_display = ('Park', 'OrganizeName', 'OrganizeID', 'Memo', 'AddContact')
    list_filter = ( 'OrganizeName', 'OrganizeID', 'Memo')
    autocomplete_fields = ['Park']
    inlines = [
        ContactsInline,
    ]

    # Tabular内联模式把多余的Original显示去除
    class Media:
        css = {"all": ("css/HideAdminOriginal.css",)}

# 3.3 、组织注册
admin.site.register(Organization, OrganizationAdmin)
