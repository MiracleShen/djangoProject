from django.contrib import admin
from Miracle.admin import ExportExcelMixin
from .models import Task
from django.utils.html import format_html


# Register your models here.
class TaskAdmin(admin.ModelAdmin, ExportExcelMixin):
    fields = ('tasktype','name', 'content', 'status')
    search_fields = ('tasktype','name', 'content', 'status')
    list_display = ('tasktype','name', 'short_content', 'colored_status','createdtime','updatedtime')
    list_filter = ('tasktype','status','createdtime','updatedtime')
    list_per_page = 10
    actions = ['export_as_excel']
    ordering = ['-updatedtime']



admin.site.register(Task, TaskAdmin)
