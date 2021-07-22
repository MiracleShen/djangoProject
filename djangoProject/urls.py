"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.staticfiles.views import serve
from django.urls import path, include, re_path
from Miracle import views as MiracleViews
from crm import views as crmViews
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from Miracle.models import MiracleNumber



class MiracleNumberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MiracleNumber
        fields = ['Zip', 'Number', 'Stars', 'Operator', 'Organize']


# Serializers define the API representation.
class MiracleNumberViewSet(viewsets.ModelViewSet):
    queryset = MiracleNumber.objects.all()
    serializer_class = MiracleNumberSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'MiracleNumber', MiracleNumberViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

def return_static(request, path, insecure=True, **kwargs):
    return serve(request, path, insecure, **kwargs)


admin.autodiscover()
urlpatterns = [
    re_path(r'^static/(?P<path>.*)$', return_static, name='static'),
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),
    path("Miracle/", MiracleViews.hello),
    path("makecall/", MiracleViews.makecall),
    path('Miracle/MiracleNumber/', MiracleViews.MiracleNumber_search, name='MiracleNumber_search'),
    path('Miracle/MiracleOrders/', MiracleViews.MiracleOrder_search, name='MiracleOrders_search'),
    path('crm/Contacts/', crmViews.Contacts_search, name='Contacts_search'),
    path('crm/Oblist/', crmViews.Oblist_search, name='Oblist_search'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
