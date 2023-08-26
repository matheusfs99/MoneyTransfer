from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import AccountViewSet, TransactionHistoryViewSet

router = DefaultRouter()
router.register("account", AccountViewSet)
router.register("transactions", TransactionHistoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
