from django.contrib import admin
from .models import *


# Register your models here.
class ContactHistoryAdmin(admin.ModelAdmin):
    fields = ('Contact', 'ContactMedia', 'Memo')
    search_fields = ('Contact__Name', 'ContactDateTime', 'ContactMedia', 'Memo')
    list_display = ('Contact', 'ContactDateTime', 'ContactMedia', 'Memo')
    list_filter = ('Contact', 'ContactDateTime', 'ContactMedia', 'Memo')
    autocomplete_fields = ['Contact']

admin.site.register(ContactHistory, ContactHistoryAdmin)


class ContactsAdmin(admin.ModelAdmin):
    fields = ('Organize','Name', 'Mobile', 'Email', 'Memo')
    search_fields = ('Organize__OrganizeName','Name', 'Mobile', 'Email', 'Memo')
    list_display = ('Organize','Name', 'Mobile', 'Email', 'Memo')
    list_filter = ('Organize','Name', 'Mobile', 'Email', 'Memo')
    autocomplete_fields = ['Organize']

admin.site.register(Contacts, ContactsAdmin)


class OrganizationAdmin(admin.ModelAdmin):
    fields = ('OrganizeName', 'OrganizeID', 'Memo')
    search_fields = ('OrganizeName', 'OrganizeID', 'Memo')
    list_display = ('OrganizeName', 'OrganizeID', 'Memo')
    list_filter = ('OrganizeName', 'OrganizeID', 'Memo')


admin.site.register(Organization, OrganizationAdmin)
