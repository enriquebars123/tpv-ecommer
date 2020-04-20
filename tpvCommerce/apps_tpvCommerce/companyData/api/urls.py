""" Urls CompanyData """

# Django Rest Framework
from rest_framework import routers

# Django
from django.conf.urls import url

# Views
from apps_tpvCommerce.companyData.api.views import (
    CityViewSet, ZoneViewSet, DealerViewSet
)

router = routers.DefaultRouter()
router.register(r'^api/v1/companyData/cities', CityViewSet)
router.register(r'^api/v1/companyData/zones', ZoneViewSet)
router.register(r'^api/v1/companyData/dealers', DealerViewSet)

urlpatterns = router.urls
