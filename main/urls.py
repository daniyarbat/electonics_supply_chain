from rest_framework.routers import DefaultRouter

from main.apps import MainConfig
from main.views import SupplierViewSet, NetworkViewSet, ProductViewSet

app_name = MainConfig.name

router = DefaultRouter()
router.register(r'supplier', SupplierViewSet, basename='supplier')
router.register(r'product', ProductViewSet, basename='product')
router.register(r'network', NetworkViewSet, basename='network')

urlpatterns = router.urls
