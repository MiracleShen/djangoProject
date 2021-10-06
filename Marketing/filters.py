import django_filters
from .models import Oblist
class OblistFilter(django_filters.FilterSet):
    Name = django_filters.CharFilter(field_name='Name',lookup_expr='icontains', label="名称")
    Phone1 = django_filters.CharFilter(field_name='Phone1',lookup_expr='icontains', label="号码1")
    Phone2 = django_filters.CharFilter(field_name='Phone2',lookup_expr='icontains', label="号码2")
    Status = django_filters.CharFilter(field_name='Status',lookup_expr='icontains', label="状态")
    Memo = django_filters.CharFilter(field_name='Memo',lookup_expr='icontains', label="备注")

    class Meta:
        model = Oblist
        fields={

        }
