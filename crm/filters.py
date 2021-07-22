import django_filters
from .models import Contacts,Oblist
class ContactsFilter(django_filters.FilterSet):
    # Organize =     Number = django_filters.CharFilter(field_name='Organize', label="组织")
    Name = django_filters.CharFilter(field_name='Name',lookup_expr='icontains', label="姓名")
    Mobile = django_filters.CharFilter(field_name='Mobile',lookup_expr='icontains', label="电话")
    Email = django_filters.CharFilter(field_name='Email',lookup_expr='icontains', label="电子邮箱")
    Memo = django_filters.CharFilter(field_name='Memo',lookup_expr='icontains', label="备注")

    class Meta:
        model = Contacts
        fields={

        }
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
