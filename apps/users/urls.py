from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet

router = DefaultRouter()
router.register("", ProfileViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
