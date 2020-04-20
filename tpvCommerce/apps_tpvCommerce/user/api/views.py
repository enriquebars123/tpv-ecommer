"""Views de usuarios"""


# Django REST Framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
# from django.shortcuts import get_object_or_404
from rest_framework import status


# serializer
from apps_tpvCommerce.user.api.serializers import userSerializers
from apps_tpvCommerce.user.api.serializers import peopleSerializers

# Models
from apps_tpvCommerce.user.models import user
from apps_tpvCommerce.user.models import people


# Utilerias
from tpvCommerce.utilerias import GeneralViewSetMixin


class UserViewSet(GeneralViewSetMixin, ModelViewSet):
    filter_fields = ['username', 'email', 'name']
    filter_backends = [DjangoFilterBackend, ]
    queryset = user.objects.all()
    serializer_class = userSerializers


class PeopleViewSet(GeneralViewSetMixin, ModelViewSet):
    queryset = people.objects.all()
    serializer_class = peopleSerializers
