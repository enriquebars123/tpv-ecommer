""" Views de CompanyData """

# Django Rest
from rest_framework.viewsets import ModelViewSet
# from rest_framework.response import Response

# Serializers
from apps_tpvCommerce.companyData.api.serializers import (
    citySerializer, zoneSerializer, dealerSerializer
)

# Models
from apps_tpvCommerce.companyData.models import (
    city, zone, dealer
)

# Utilerias
from tpvCommerce.utilerias import GeneralViewSetMixin


class CityViewSet(GeneralViewSetMixin, ModelViewSet):
    queryset = city.objects.all()
    serializer_class = citySerializer


class ZoneViewSet(GeneralViewSetMixin, ModelViewSet):
    queryset = zone.objects.all()
    serializer_class = zoneSerializer


class DealerViewSet(GeneralViewSetMixin, ModelViewSet):
    queryset = dealer.objects.all()
    serializer_class = dealerSerializer
