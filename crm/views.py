from django.shortcuts import render
from .filters import ContactsFilter, OblistFilter
from .models import Contacts, Oblist, Status, OWNERS
from django.db.models import Count
from django.core.paginator import Paginator
from jinja2 import Environment, FileSystemLoader
from pyecharts.globals import CurrentConfig
from django.http import HttpResponse
from Miracle.models import MiracleNumber
from django.db import models

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
        y1 = []
        for y in OWNERS.values:
            A = Oblist.objects.filter(Owner=y).filter(Status=x)
            y1.append(A.count())
        bar = bar.add_yaxis(x, y1)
    c = (
        bar
    )
    return HttpResponse(c.render_embed())


class OPERATORS(models.TextChoices):
    CM = '中国移动', '中国移动'
    CU = '中国联通', '中国联通'
    CT = '中国电信', '中国电信'


class STATUSS(models.TextChoices):
    AA = '可选', '可选'
    BB = '锁定', '锁定'
    CC = '已售', '已售'


def NumberReport(request):
    bar = Bar().add_xaxis(OPERATORS.values).set_global_opts(
        title_opts=opts.TitleOpts(title="数据报表", subtitle="所有数据"))
    for x in STATUSS.values:
        print(x)
        y1 = []
        for y in OPERATORS.values:
            print(y)
            A = MiracleNumber.objects.filter(Operator=y).filter(Status=x)
            print(A)
            y1.append(A.count())
        bar = bar.add_yaxis(x, y1)
    c = (
        bar
    )
    return HttpResponse(c.render_embed())


def NumberOrganizeReport(request):
    ORG = MiracleNumber.objects.filter().exclude(Organize='无').values('Organize').annotate(Org_num=Count('id')).values(
        'Organize', 'Org_num').order_by('Org_num')
    x1 = []
    for x in ORG:
        x1.append(x['Organize'])
    bar = Bar(init_opts=opts.InitOpts(height='900px',width="1500px")).add_xaxis(x1).set_global_opts(
        title_opts=opts.TitleOpts(title="数据报表", subtitle="所有数据"),
        yaxis_opts=opts.AxisOpts(name_rotate=60, axislabel_opts={"rotate": 45}),
        # legend_opts=opts.LegendOpts(is_show=False),
    ).reversal_axis()
    y1 = []
    for y in ORG:
        A = MiracleNumber.objects.filter(Organize=y['Organize'])
        y1.append(A.count())
    bar = bar.add_yaxis('号码数', y1, bar_width="80%", category_gap="30%",).set_series_opts(
        label_opts=opts.LabelOpts(position="right"))
    c = (
        bar
    )
    return HttpResponse(c.render_embed())
