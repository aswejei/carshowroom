from rest_framework.routers import DefaultRouter

from supplier.views import CarPriceRelationSupplierViewSet
from supplier.views import SupplierViewSet

router = DefaultRouter()
router.register('suppliers', SupplierViewSet)
router.register('prices', CarPriceRelationSupplierViewSet)

urlpatterns = []
urlpatterns += router.urls



