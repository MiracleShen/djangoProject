from django.contrib import admin
from .models import *


# Register your models here.
class ContactsAdmin(admin.ModelAdmin):
    fields = ('Name', 'Mobile', 'Email', 'Memo')
    search_fields = ('Name', 'Mobile', 'Email', 'Memo')
    list_display = ('Name', 'Mobile', 'Email', 'Memo')
    list_filter = ('Name', 'Mobile', 'Email', 'Memo')


admin.site.register(Contacts, ContactsAdmin)


class OrganizationAdmin(admin.ModelAdmin):
    fields = ('OrganizeName', 'OrganizeID', 'Memo')
    search_fields = ('OrganizeName', 'OrganizeID', 'Memo')
    list_display = ('OrganizeName', 'OrganizeID', 'Memo')
    list_filter = ('OrganizeName', 'OrganizeID', 'Memo')


admin.site.register(Organization, OrganizationAdmin)
