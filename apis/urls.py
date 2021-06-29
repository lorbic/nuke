from django.urls.conf import include, path
from rest_framework import routers

from apis.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]