from django.shortcuts import render
from .filters import ContactsFilter, OblistFilter
from .models import Contacts, Oblist,Status,OWNERS
from django.db.models import Count
from django.core.paginator import Paginator
from jinja2 import Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig
from django.http import HttpResponse

CurrentConfig.GLOBAL_ENV = Environment(loader=FileSystemLoader("./crm/templates"))
from pyecharts import options as opts
from pyecharts.charts import Bar


# Create your views here.
def Contacts_search(request):
    f = ContactsFilter(request.GET, queryset=Contacts.objects.all())
    paginator = Paginator(f.qs, 20)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    context = {'page_obj': page_obj, 'paginator': paginator,
               'is_paginated': True, 'filter': f, }
    return render(request, 'Contacts_filter.html', context)


def Oblist_search(request):
    f = OblistFilter(request.GET, queryset=Oblist.objects.all())
    paginator = Paginator(f.qs, 20)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    context = {'page_obj': page_obj, 'paginator': paginator,
               'is_paginated': True, 'filter': f, }
    return render(request, 'Oblist_filter.html', context)


def index(request):
    bar = Bar().add_xaxis(OWNERS.values).set_global_opts(title_opts=opts.TitleOpts(title="数据报表", subtitle="所有数据"))
    for x in Status.values:
        y1 =[]
        for y in OWNERS.values:
            A = Oblist.objects.filter(Owner=y).filter(Status=x)
            y1.append(A.count())
        bar = bar.add_yaxis(x,y1)
    c = (
        bar
    )
    return HttpResponse(c.render_embed())
