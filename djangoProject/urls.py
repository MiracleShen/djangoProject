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
from django.urls import path,include,re_path
from Miracle import views as MiracleViews
from django.contrib import admin
def return_static(request, path, insecure=True, **kwargs):
  return serve(request, path, insecure, **kwargs)
admin.autodiscover()
urlpatterns = [
    re_path(r'^static/(?P<path>.*)$', return_static, name='static'),
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),
    path("Miracle/",MiracleViews.hello),
    path("makecall/", MiracleViews.makecall),
    path('Miracle/MiracleNumber/',MiracleViews.MiracleNumber_search,name='MiracleNumber_search'),
    path('Miracle/MiracleOrders/', MiracleViews.MiracleOrder_search, name='MiracleOrders_search')
]
