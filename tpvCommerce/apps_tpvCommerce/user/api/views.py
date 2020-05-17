"""Views de usuarios"""


# Django REST Framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
#from django.shortcuts import get_object_or_404
from rest_framework import status


# serializer
from apps_tpvCommerce.user.api.serializers import userSerializers
from apps_tpvCommerce.user.api.serializers import peopleSerializers
from apps_tpvCommerce.user.api.serializers import submenuSerializers
from apps_tpvCommerce.user.api.serializers import menuSerializers
from apps_tpvCommerce.user.api.serializers import profileSerializer

# Models
from apps_tpvCommerce.user.models import user
from apps_tpvCommerce.user.models import people
from apps_tpvCommerce.user.models import submenu
from apps_tpvCommerce.user.models import menu
from apps_tpvCommerce.user.models import profile


# Utilerias
from tpvCommerce.utilerias import GeneralViewSetMixin


class UserViewSet(GeneralViewSetMixin, ModelViewSet):
    filter_fields = ['username', 'email', 'name']
    filter_backends = [DjangoFilterBackend,]
    queryset = user.objects.all()
    serializer_class = userSerializers


class PeopleViewSet(GeneralViewSetMixin, ModelViewSet):
    queryset = people.objects.all()
    serializer_class = peopleSerializers

class SubmenuViewSet(GeneralViewSetMixin, ModelViewSet):
    queryset = submenu.objects.all()
    serializer_class = submenuSerializers

class MenuViewSet(GeneralViewSetMixin, ModelViewSet):
    queryset = menu.objects.all()
    serializer_class = menuSerializers

class ProfileViewSet(GeneralViewSetMixin, ModelViewSet):
    queryset = profile.objects.all()
    serializer_class = profileSerializer