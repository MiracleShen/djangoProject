import django_filters

import crm.models
from Miracle.models import MiracleNumber,MiracleOrders
class MiracleNumberFilter(django_filters.FilterSet):
    Zip = django_filters.CharFilter(field_name='Zip',
                                  lookup_expr='icontains', label="区号")
    Number = django_filters.CharFilter(field_name='Number',
                                  lookup_expr='icontains', label="号码")
    Stars = django_filters.ChoiceFilter(field_name='Stars',
                                  choices=MiracleNumber.STAR)
    Operator = django_filters.ChoiceFilter(field_name='Operator',choices=MiracleNumber.OPERATORS)
    Status = django_filters.ChoiceFilter(field_name='Status',choices=MiracleNumber.STATUSS)
    class Meta:
        model = MiracleNumber
        fields={

        }
class MiracleOrderFilter(django_filters.FilterSet):
    CustomerName = django_filters.ModelChoiceFilter(queryset=crm.models.Organization.objects.all(),
                                  label="客户名称")
    OrderDate = django_filters.DateTimeFilter(field_name='OrderDate',lookup_expr='gte',label='下单日期'
                                              )
    class Meta:
        model = MiracleOrders
        fields=[

        ]