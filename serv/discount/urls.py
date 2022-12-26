from rest_framework.routers import DefaultRouter

from serv.discount.views import ShowroomDiscountViewSet, SupplierDiscountViewSet

router = DefaultRouter()
router.register('showrooms', ShowroomDiscountViewSet)
router.register('suppliers', SupplierDiscountViewSet)

urlpatterns = []
urlpatterns += router.urls
