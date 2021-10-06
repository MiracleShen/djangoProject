from .models import MiracleNumber, MiracleOrders, MiracleBill, MiracleCredit, MiracleDID, MiraclePBX
from django.shortcuts import render, HttpResponse
import datetime
from django.db.models import Sum

def Cal(req):
    context = {}
    qs = MiracleOrders.objects.values("CustomerName__id", "CustomerName", "CustomerName__OrganizeName").distinct()
    ### 获取当前时间，年份，月份
    date = datetime.datetime.now()
    print(date.year, date.month, date.day)
    YEAR = date.year
    MONTH = date.month - 1
    for i in qs:
        ### 把组织的所有订单计算的金额赋值给i[CustomerName']，qs传参给context，在网页端渲染。
        # print (i['CustomerName__OrganizeName'],OrgCal(i['CustomerName']))
        i['CustomerName'] = OrgCal(i['CustomerName'])
        print(i['CustomerName'])
        ### 从MiracleBill中查询当月记录，如果存在，则Update；如果不存在，则Create
        qs_bill = MiracleBill.objects.filter(CustomerID=i['CustomerName__id'], Year=YEAR, Month=MONTH)
        if qs_bill:
            print(i['CustomerName__id'], '有数据')
        else:
            print(i['CustomerName__id'], '无数据')
            qs_bill.create(
                Year=YEAR,
                Month=MONTH,
                Bill_Cycle='月度',
                Bill_Type='租金',
                Bill=i['CustomerName'],
                CustomerID_id=i['CustomerName__id'],
                Bill_Status='未出账',
                Memo=str(YEAR) + '年' + str(MONTH) + '月租金'
            )
        # print (i.CustomerName__OrganizeName,OrgCal(i.CustomerName__OrganizeName))
    ### 检查渲染前的数据，赋值给context
    print(qs)
    context['qs'] = qs
    return render(req, "MiracleCal.html", context)


def OrgCal(CN):
    ## 根据传进来的CustomerID过滤MiracleOrders数据集
    qs = MiracleOrders.objects.filter(CustomerName=CN)
    ## 把客户下所有的订单的月租都算出来，相加，就得出了这个客户所有的订单的月租。
    MRent = 0
    for i in qs:
        ## 订单计算需要传入两个参数，一个是id，一个是订单类型
        MRent = MRent + OrdCal(i.id, i.OrderType)
    return MRent


def OrdCal(id, OrderType):
    ## 根据传入的ID来获取MiracleOrders
    qs = MiracleOrders.objects.filter(id=id)
    ## 根据订单类型计算当月月租
    ## 如果是退订，就是负值；如果是新增，就是正值
    Rent = 0
    for i in qs:
        if OrderType == '退订':
            Rent = Rent + i.APP_Number * 10 + i.SIP_Number * 10 + i.CC_Number * 30 + i.Log_Number * 30 + i.HPR_Number * 10
            Rent = Rent + i.Number_0 * 35 + i.Number_1 * 100 + i.Number_2 * 200 + i.Number_3 * 500 + i.Line_Number * 100
            if i.PBX_Type == '免费版':
                Rent = Rent + 0
            elif i.PBX_Type == '查询版':
                Rent = Rent + 30
            elif i.PBX_Type == '管理版':
                Rent = Rent + 300
            elif i.PBX_Type == '本地部署版':
                Rent = Rent + 1200
            else:
                print('交换机版本设置有误，目前只有免费版、查询版、管理版、本地部署版')
            Rent = -Rent
        else:
            Rent = Rent + i.APP_Number * 10 + i.SIP_Number * 10 + i.CC_Number * 30 + i.Log_Number * 30 + i.HPR_Number * 10
            Rent = Rent + i.Number_0 * 35 + i.Number_1 * 100 + i.Number_2 * 200 + i.Number_3 * 500 + i.Line_Number * 100
            if i.PBX_Type == '免费版':
                Rent = Rent + 0
            elif i.PBX_Type == '查询版':
                Rent = Rent + 30
            elif i.PBX_Type == '管理版':
                Rent = Rent + 300
            elif i.PBX_Type == '本地部署版':
                Rent = Rent + 1200
            else:
                print('交换机版本设置有误，目前只有免费版、查询版、管理版、本地部署版')
    return Rent


def CallInit(req):
    ## 获取当前年月
    date = datetime.datetime.now()
    # print(date.year, date.month, date.day)
    YEAR = date.year
    MONTH = date.month - 1
    ## 生成PBX的话费账单
    qs_pbx = MiraclePBX.objects.values('Customer__id', 'Customer', 'PBX').distinct()
    for i in qs_pbx:
        print(i['Customer'])
        qs_credit = MiracleCredit.objects.filter(Customer=i['Customer'], Account=i['PBX'])
        if qs_credit:
            print(qs_credit, '有数据')
        else:
            print('无数据')
            qs_credit.create(
                Customer_id=i['Customer__id'],
                Type='PBX',
                Account=i['PBX'],
                Year=YEAR,
                Month=MONTH,
                Credit=0,
                Memo=str(YEAR) + '年' + str(MONTH) + '月通话费用'
            )
    ## 生成DID的话费账单
    qs_did = MiracleDID.objects.values('Customer__id', 'Customer', 'PBX', 'DID').distinct()
    for i in qs_did:
        print(i['Customer'])
        qs_credit = MiracleCredit.objects.filter(Customer=i['Customer'], Account=i['DID'])
        if qs_credit:
            print(qs_credit, '有数据')
        else:
            print('无数据')
            qs_credit.create(
                Customer_id=i['Customer__id'],
                Type='DID',
                Account=i['PBX'] + '.' + i['DID'],
                Year=YEAR,
                Month=MONTH,
                Credit=0,
                Memo=str(YEAR) + '年' + str(MONTH) + '月通话费用'
            )
    return HttpResponse('Ok')


def CallCal(req):
    date = datetime.datetime.now()
    # print(date.year, date.month, date.day)
    YEAR = date.year
    MONTH = date.month - 1
    # 从MiracleCredit里提取公司名称，并计算总消费金额。
    qs_credit = MiracleCredit.objects.filter(Year=YEAR,Month=MONTH).values('Customer__id','Customer').distinct()
    for i in qs_credit:
        # print (i['Customer'])
        # 检查MiracleBill里是否有该公司当月话单，如果没有，则新增话单。
        qs_Bill = MiracleBill.objects.filter(Year=YEAR,Month=MONTH,Bill_Type='话费',CustomerID=i['Customer__id'])
        if qs_Bill:
            # print('有数据')
            pass
        else:
            print('无数据')
            qs_Bill.create(
                Year=YEAR,
                Month=MONTH,
                Bill_Cycle='月度',
                Bill_Type='话费',
                Bill=CreditCal(i['Customer__id']),
                CustomerID_id=i['Customer__id'],
                Bill_Status='未出账',
                Memo=str(YEAR) + '年' + str(MONTH) + '月话费'
            )
    return HttpResponse('Ok')
def CreditCal(CustomerID):
    date = datetime.datetime.now()
    # print(date.year, date.month, date.day)
    YEAR = date.year
    MONTH = date.month - 1
    BILL=0
    qs = MiracleCredit.objects.filter(Year=YEAR,Month=MONTH,Customer=CustomerID)
    for i in qs:
        BILL=BILL+i.Credit
    # print (CustomerID,'话费记录数',qs.count())
    # qs.aggregate(BILL=Sum('Credit'))
    #
    # print(BILL)
    return BILL