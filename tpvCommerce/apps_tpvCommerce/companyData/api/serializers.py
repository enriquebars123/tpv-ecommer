""" CompanyData Serializers """


# Django Rest
from rest_framework import serializers
import django_filters

# Models
from apps_tpvCommerce.companyData.models import *


class countrySerializer(serializers.ModelSerializer):
    class Meta:
        model = country
        fields = "__all__"


class townshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = township
        fields = "__all__"


class dealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = dealer
        fields = "__all__"
