""" Views de CompanyData """

# Django Rest
from rest_framework.viewsets import ModelViewSet
# from rest_framework.response import Response

# Serializers
from apps_tpvCommerce.companyData.api.serializers import *

# Models
from apps_tpvCommerce.companyData.models import *

# Utilerias
from tpvCommerce.utilerias import GeneralViewSetMixin


class CountryViewSet(GeneralViewSetMixin, ModelViewSet):
    queryset = country.objects.all()
    serializer_class = countrySerializer


class TownshipViewSet(GeneralViewSetMixin, ModelViewSet):
    queryset = township.objects.all()
    serializer_class = townshipSerializer


class DealerViewSet(GeneralViewSetMixin, ModelViewSet):
    queryset = dealer.objects.all()
    serializer_class = dealerSerializer
