""" Registro urls """

# Django REST Framework
from rest_framework import routers

# Django
from django.conf.urls import url

# Views
from apps_tpvCommerce.user.api.views import UserViewSet
from apps_tpvCommerce.user.api.views import PeopleViewSet
from apps_tpvCommerce.user.api.views import SubmenuViewSet
from apps_tpvCommerce.user.api.views import MenuViewSet
from apps_tpvCommerce.user.api.views import ProfileViewSet

router = routers.DefaultRouter()
router.register(r'^api/v1/user', UserViewSet)
router.register(r'^api/v1/people', PeopleViewSet)
router.register(r'^api/v1/submenu', SubmenuViewSet)
router.register(r'^api/v1/menu', MenuViewSet)
router.register(r'^api/v1/profile', ProfileViewSet)

urlpatterns = router.urls
