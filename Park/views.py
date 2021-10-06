from django.shortcuts import render
from django.shortcuts import render, HttpResponse
import requests
import datetime, json, ast
from .models import Park
# Create your views here.
def GetTown(req):
    context = {}
    ADDRESS=''
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
    # print (res2)
    res22 = json.loads(res2.text)
    # print (res22)
    res23 = str(res22['result']['location']['lat'])+','+str(res22['result']['location']['lng'])
    # 根据坐标获得所在的国家、省份、城市、区县、乡镇、街道
    URL3 = 'https://api.map.baidu.com/reverse_geocoding/v3/'
    ####测试行级按钮获得六级地址
    print ('Status的值是：',req.GET.get('id',0),req.GET.get('status',88))
    XY = req.GET.get('status',88)
    XY =str(XY)
    print (XY)
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
    add=json.loads(res3.text)['result']
    add1 =add['addressComponent']['province']+add['addressComponent']['city']+add['addressComponent']['district']+add['addressComponent']['town']
    context['res23']=res23

    context['ADDRESS']=ADDRESS
    if 'id' in req.GET and req.GET['id']:
        qs=Park.objects.get(id=req.GET['id'])
        qs.Province=add['addressComponent']['province']
        qs.City=add['addressComponent']['city']
        qs.District=add['addressComponent']['district']
        qs.Street=add['addressComponent']['town']
        qs.save()
    # return render(req,"a_hello.html", context)
    #####测试行级按钮获取六级地址
    return HttpResponse(add1)
