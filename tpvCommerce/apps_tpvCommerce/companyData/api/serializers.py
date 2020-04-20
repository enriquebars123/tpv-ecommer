""" CompanyData Serializers """


# Django Rest
from rest_framework import serializers
import django_filters

# Models
from apps_tpvCommerce.companyData.models import (
    city, dealer, zone
)


class zoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = zone
        fields = "__all__"


class citySerializer(serializers.ModelSerializer):

    class Meta:
        model = city
        fields = "__all__"


class dealerSerializer(serializers.ModelSerializer):

    class Meta:
        model = dealer
        fields = "__all__"
