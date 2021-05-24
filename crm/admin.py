from django.contrib import admin
from .models import *


# Register your models here.
class ContactHistoryAdmin(admin.ModelAdmin):
    fields = ('Name', 'ContactDateTime', 'ContactMedia', 'Memo')
    search_fields = ('Name', 'ContactDateTime', 'ContactMedia', 'Memo')
    list_display = ('Name', 'ContactDateTime', 'ContactMedia', 'Memo')
    list_filter = ('Name', 'ContactDateTime', 'ContactMedia', 'Memo')


admin.site.register(ContactHistory, ContactHistoryAdmin)


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
