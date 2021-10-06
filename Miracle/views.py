from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponse
from .models import MiracleNumber, MiracleOrders
from .filters import MiracleNumberFilter, MiracleOrderFilter
from django.db.models import Sum
import datetime, json, ast
from urllib import request, parse
import ssl
from .CalBill import *
from django.views.decorators.csrf import csrf_exempt
ssl._create_default_https_context = ssl._create_unverified_context
import requests


# Create your views here.

def hello(req):
    CITY='上海'
    if 'City' in req.GET and req.GET['City']:
        CITY = req.GET['City']
    URL = 'http://api.map.baidu.com/api_region_search/v1/'

    params = {
        "ak": 'Xmjf4HD2kly5zqZybYhmZV9RW7fx7ass',
        "keyword": CITY,
        "sub_admin": 3
    }
    res = requests.get(url=URL, params=params)
    context = {}
    context['res'] = json.loads(res.text)
    ADDRESS='上海中心大厦'
    if 'Address' in req.GET and req.GET['Address']:
        ADDRESS = req.GET['Address']
    # 根据园区名称获得坐标
    URL2 = 'https://api.map.baidu.com/geocoding/v3/'
    params2 = {
        "ak": 'Xmjf4HD2kly5zqZybYhmZV9RW7fx7ass',
        "output": 'json',
        "address" : ADDRESS,
        "ret_coordtype": 'bd09II',
    }
    res2= requests.get(url=URL2, params=params2)
    print (res2)
    res22 = json.loads(res2.text)
    print (res22)
    res23 = str(res22['result']['location']['lat'])+','+str(res22['result']['location']['lng'])
    # 根据坐标获得所在的国家、省份、城市、区县、乡镇、街道
    URL3 = 'https://api.map.baidu.com/reverse_geocoding/v3/'
    ####测试行级按钮获得六级地址
    # print ('Status的值是：',req.GET.get('id',0),req.GET.get('status',88))
    # XY = req.GET.get('status',88)
    # XY =str(XY)
    # print (XY)
    params3 = {
        "ak": 'Xmjf4HD2kly5zqZybYhmZV9RW7fx7ass',
        "output": 'json',
        "coordtype":'bd09II',
        "ret_coordtype":'bd09II',
        "extensions_town": "true",
        "extensions_road":"true",
        "location":res23,
        "sub_admin": 3
    }
    res3 = requests.get(url=URL3, params=params3)
    print(res3.text)
    context['res3']=json.loads(res3.text)['result']
    #####测试行级按钮获取六级地址
    # add=json.loads(res3.text)['result']
    # add1 =add['addressComponent']['province']+add['addressComponent']['city']+add['addressComponent']['district']+add['addressComponent']['town']
    context['res23']=res23

    context['ADDRESS']=ADDRESS
    return render(req,"a_hello.html", context)
    #####测试行级按钮获取六级地址
    # return HttpResponse(add1)

@csrf_exempt
def makecall(req):
    # context = {}
    # context['test'] = 'Miracle Test'
    # print("the POST method")
    # URL = "https://sh001.ezphone.cn:8443/ucrm/api/phone/dialOutbound?para="
    # data = {"apiKey": "PYTIzDD7W9BBzvkjvYX0E6dj8nzPBnCvwQzIHC3zpPs"}
    # data["callerKey"] = "miracle.shen"
    # data["callerKeyType"] = "loginAccount"
    # data["destNumber"]=str(req.GET.get("destNumber")).replace("\n","")
    # data = parse.urlencode(data)
    # data = str(parse.parse_qs(data)).replace("'", "\"").replace("[", "").replace("]", "").replace(" ", "").replace("\n",
    #                                                                                                                "")
    # URL = URL + data
    # print(URL)
    # page = request.urlopen(URL)
    # print(page)
    # html = page.read().decode('utf-8')  # 将接收到的数据使用utf8解码
    # print(html)
    # json_data = json.loads(html)
    # print(json_data)
    # return HttpResponse(html)
    context = {}
    context['test'] = 'Miracle Test'

    if (req.method == 'POST'):
        print(req.user.username)

        URL = "https://sh001.ezphone.cn:8443/ucrm/api/phone/dialOutbound?para="
        data = {"apiKey": "PYTIzDD7W9BBzvkjvYX0E6dj8nzPBnCvwQzIHC3zpPs"}
        if (req.user.username == 'admin'):
            data["callerKey"] = 'miracle.shen'
        elif (req.user.username == 'mengmeng.geng'):
            data["callerKey"] = 'gengmengmeng'
        else:
            data["callerKey"] = req.user.username
        data["callerKeyType"] = "loginAccount"
        data["destNumber"] = str(req.POST["destNumber"]).replace("\n", "")
        data = parse.urlencode(data)
        data = str(parse.parse_qs(data)).replace("'", "\"").replace("[", "").replace("]", "").replace(" ", "").replace(
            "\n",
            "")
        URL = URL + data
        print(URL)
        page = request.urlopen(URL)
        print(page)
        html = page.read().decode('utf-8')  # 将接收到的数据使用utf8解码
        print(html)
        json_data = json.loads(html)
        print(json_data)
    return HttpResponse(html)
def MiracleNumber_search(request):
    f = MiracleNumberFilter(request.GET, queryset=MiracleNumber.objects.filter(Status='可选').order_by('-Stars'))
    paginator = Paginator(f.qs, 20)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    context = {'page_obj': page_obj, 'paginator': paginator,
               'is_paginated': True, 'filter': f, }

    return render(request, 'MiracleNumber_filter.html', context)
def MonthlyRent(request):
    CS = '金开区'
    f = MiracleOrderFilter(request.GET, queryset=MiracleOrders.objects.filter(CustomerName__OrganizeName__icontains=CS).order_by('-OrderDate'))
    paginator = Paginator(f.qs, 20)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    context = {'page_obj': page_obj, 'paginator': paginator,
               'is_paginated': True, 'filter': f, }
    # Miracle Number月租计算
    context['Number_Total'] = f.qs.aggregate(
        Number_Total=Sum('Number_0') * 35 + Sum('Number_1') * 100 + Sum('Number_2') * 200 + Sum('Number_3') * 500 + Sum(
            'Number_4') * 2000 + Sum('Number_5') * 5000 + Sum('Line_Number') * 35)
    # Miracle Phone月租（含硬件话机租赁)计算
    context['Phone_Total'] = f.qs.aggregate(
        Phone_Total=Sum('APP_Number') * 10 + Sum('SIP_Number') * 10 + Sum('Log_Number') * 30 + Sum('CC_Number') * 30 + Sum(
            'HPR_Number') * 10)
    # Miracle PBX租金计算
    for i in f.qs.values('PBX_Type'):
        PBX_Sum=0
        if i['PBX_Type'] == '免费版':
            PBX_Sum = PBX_Sum + 0
        elif i['PBX_Type'] == '查询版':
            PBX_Sum= PBX_Sum + 30
        elif i['PBX_Type'] == '管理版':
            PBX_Sum = PBX_Sum + 300
        elif i['PBX_Type'] == '本地部署版':
            PBX_Sum = PBX_Sum + 1200
        else:
            print('交换机版本设置有误，目前只有免费版、查询版、管理版、本地部署版')
    # Miracle MCU租金计算
    for i in f.qs.values('MCU_Type'):
        MCU_Sum =0
        if i['MCU_Type'] == '无':
            MCU_Sum = MCU_Sum + 0
        elif i['MCU_Type'] == '有':
            MCU_Sum = MCU_Sum + 300
        else:
            print('MCU设置有误，目前只有有和无')
    # Miracle API租金计算
    for i in f.qs.values('API_Type'):
        API_Sum =0
        if i['API_Type'] == '无':
            context['API_Sum'] = API_Sum + 0
        elif i['API_Type'] == '有':
            API_Sum = API_Sum+ 1000
        else:
            print('API设置有误，目前只有有和无')
    context['PBX_Total']=PBX_Sum+MCU_Sum+API_Sum
    context['Total']=context['Number_Total']['Number_Total']+context['Phone_Total']['Phone_Total']+context['PBX_Total']
    return render(request, 'MonthlyRent_filter.html', context)
# Miracle订单分析，可以展示Miracle订单产生的总的月租表，也可以看出每一类、每一项产品所产生的月租收入情况。
def MiracleOrder_search(request):

    f = MiracleOrderFilter(request.GET, queryset=MiracleOrders.objects.all().order_by('-OrderDate'))
    # 分页处理
    paginator = Paginator(f.qs, 10)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    contexts = {'page_obj': page_obj, 'paginator': paginator,
                'is_paginated': True, 'filter': f, }
    # 参数赋值
    contexts['PBX_Sum'] = 0
    contexts['MCU_Sum'] = 0
    contexts['API_Sum'] = 0

    # Miracle Number 费用计算
    contexts['Number_0_Sum'] = f.qs.aggregate(Number_0_Sum=Sum('Number_0'))
    contexts['Number_1_Sum'] = f.qs.aggregate(Number_1_Sum=Sum('Number_1'))
    contexts['Number_2_Sum'] = f.qs.aggregate(Number_2_Sum=Sum('Number_2'))
    contexts['Number_3_Sum'] = f.qs.aggregate(Number_3_Sum=Sum('Number_3'))
    contexts['Number_4_Sum'] = f.qs.aggregate(Number_4_Sum=Sum('Number_4'))
    contexts['Number_5_Sum'] = f.qs.aggregate(Number_5_Sum=Sum('Number_5'))
    contexts['Line_Number_Sum'] = f.qs.aggregate(Line_Number_Sum=Sum('Line_Number'))
    contexts['Number_Total'] = f.qs.aggregate(
        Number_Total=Sum('Number_0') * 35 + Sum('Number_1') * 100 + Sum('Number_2') * 200 + Sum('Number_3') * 500 + Sum(
            'Number_4') * 2000 + Sum('Number_5') * 5000 + Sum('Line_Number') * 35)
    # Miracle PBX 费用计算
    for i in f.qs.values('PBX_Type'):
        if i['PBX_Type'] == '免费版':
            contexts['PBX_Sum'] = contexts['PBX_Sum'] + 0
        elif i['PBX_Type'] == '查询版':
            contexts['PBX_Sum'] = contexts['PBX_Sum'] + 30
        elif i['PBX_Type'] == '管理版':
            contexts['PBX_Sum'] = contexts['PBX_Sum'] + 300
        elif i['PBX_Type'] == '本地部署版':
            contexts['PBX_Sum'] = contexts['PBX_Sum'] + 1200
        else:
            print('交换机版本设置有误，目前只有免费版、查询版、管理版、本地部署版')

    for i in f.qs.values('MCU_Type'):
        if i['MCU_Type'] == '无':
            contexts['MCU_Sum'] = contexts['MCU_Sum'] + 0
        elif i['MCU_Type'] == '有':
            contexts['MCU_Sum'] = contexts['MCU_Sum'] + 300
        else:
            print('MCU设置有误，目前只有有和无')

    for i in f.qs.values('API_Type'):
        if i['API_Type'] == '无':
            contexts['API_Sum'] = contexts['API_Sum'] + 0
        elif i['API_Type'] == '有':
            contexts['API_Sum'] = contexts['API_Sum'] + 1000
        else:
            print('API设置有误，目前只有有和无')
    # Miracle Phone 费用计算

    contexts['APP_Sum'] = f.qs.aggregate(APP_Sum=Sum('APP_Number'))
    contexts['SIP_Sum'] = f.qs.aggregate(SIP_Sum=Sum('SIP_Number'))
    contexts['Log_Sum'] = f.qs.aggregate(Log_Sum=Sum('Log_Number'))
    contexts['CC_Sum'] = f.qs.aggregate(CC_Sum=Sum('CC_Number'))
    contexts['HPR_Sum'] = f.qs.aggregate(HPR_Sum=Sum('HPR_Number'))
    contexts['Total'] = f.qs.aggregate(
        Total=Sum('APP_Number') * 10 + Sum('SIP_Number') * 10 + Sum('Log_Number') * 30 + Sum('CC_Number') * 30 + Sum(
            'HPR_Number') * 10)
    # contexts['result'] = a
    return render(request, 'MiracleOrder_filter.html', contexts)
