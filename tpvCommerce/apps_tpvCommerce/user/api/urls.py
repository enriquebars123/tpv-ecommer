""" Registro urls """

# Django REST Framework
from rest_framework import routers

# Django
from django.conf.urls import url

# Views
from apps_tpvCommerce.user.api.views import UserViewSet
from apps_tpvCommerce.user.api.views import PeopleViewSet

router = routers.DefaultRouter()
router.register(r'^api/v1/user', UserViewSet)
router.register(r'^api/v1/people', PeopleViewSet)

urlpatterns = router.urls
