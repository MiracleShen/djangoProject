from django.contrib import admin
from .models import *


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
    fields = ('Organize', 'Name', 'Mobile', 'Email', 'Memo')
    search_fields = ('Organize__OrganizeName', 'Name', 'Mobile', 'Email', 'Memo')
    list_display = ('Organize', 'Name', 'Mobile', 'Email', 'Memo')
    list_filter = ('Organize', 'Name', 'Mobile', 'Email', 'Memo')
    autocomplete_fields = ['Organize']


admin.site.register(Contacts, ContactsAdmin)


class OrganizationAdmin(admin.ModelAdmin):
    fields = ('OrganizeName', 'OrganizeID', 'Memo')
    search_fields = ('OrganizeName', 'OrganizeID', 'Memo')
    list_display = ('OrganizeName', 'OrganizeID', 'Memo')
    list_filter = ('OrganizeName', 'OrganizeID', 'Memo')


admin.site.register(Organization, OrganizationAdmin)

class OblistAdmin(admin.ModelAdmin):
    fields = ('Campaign', 'Name', 'Phone1', 'Phone2', 'Status', 'Memo','Owner')
    search_fields = ('Campaign', 'Name', 'Phone1', 'Phone2', 'Status', 'Memo','Owner')
    list_display = ('Campaign', 'Name', 'Phone1', 'Phone2', 'Status','colored_Status', 'Memo','Owner', 'makecall')
    list_filter = ('Campaign', 'Name', 'Phone1', 'Phone2', 'Status', 'Memo','Owner')
    list_editable = ('Status','Owner')
    def makecall(self,obj):
        # html = '<a target="blank" href="/makecall/?destNumber='
        # html = html + obj.Phone1
        # html = html +'">拨打<a/>'
        html = '<button onclick="makecall('
        html = html + obj.Phone1
        html = html +')">拨打1</button>'
        if  obj.Phone2 :
            print ('我有老二：'+obj.Phone2)
            html = html + '<button onclick="makecall('
            html = html + obj.Phone2
            html = html +')">拨打2</button>'
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
