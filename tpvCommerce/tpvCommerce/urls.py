"""tpvCommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from apps_tpvCommerce.user.api.views import *
from apps_tpvCommerce.companyData.api.views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('api/v1/user', UserViewSet)
router.register('api/v1/people', PeopleViewSet)
router.register('api/v1/company/zone', ZoneViewSet)
router.register('api/v1/company/city', CityViewSet)
router.register('api/v1/company/dealer', DealerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    url('', include(
        ('apps_tpvCommerce.user.api.urls', 'Api_user'), namespace='Api_user')),
    url('', include(
        ('apps_tpvCommerce.companyData.api.urls', 'Api_companyData'),
        namespace='Api_companyData')),
]
