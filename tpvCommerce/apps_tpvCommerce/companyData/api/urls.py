""" Urls CompanyData """

# Django Rest Framework
from rest_framework import routers

# Django
from django.conf.urls import url

# Views
from apps_tpvCommerce.companyData.api.views import *

router = routers.DefaultRouter()
router.register(r'^api/v1/companyData/city', CountryViewSet)
router.register(r'^api/v1/companyData/zone', TownshipViewSet)
router.register(r'^api/v1/companyData/dealer', DealerViewSet)

urlpatterns = router.urls
