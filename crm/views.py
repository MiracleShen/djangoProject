from django.shortcuts import render
from .filters import ContactsFilter,OblistFilter
from .models import Contacts,Oblist
from django.core.paginator import Paginator
# Create your views here.
def Contacts_search(request):
    f = ContactsFilter(request.GET,queryset=Contacts.objects.all())
    paginator = Paginator(f.qs, 20)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    context = {'page_obj': page_obj, 'paginator': paginator,
               'is_paginated': True, 'filter': f, }
    return render(request,'Contacts_filter.html',context)

def Oblist_search(request):
    f = OblistFilter(request.GET,queryset=Oblist.objects.all())
    paginator = Paginator(f.qs, 20)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    context = {'page_obj': page_obj, 'paginator': paginator,
               'is_paginated': True, 'filter': f, }
    return render(request,'Oblist_filter.html',context)