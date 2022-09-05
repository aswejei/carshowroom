from rest_framework.routers import DefaultRouter

from carshowroom.views import CarShowroomViewSet, CarPriceRelationShowroomViewSet

router = DefaultRouter()
router.register('', CarShowroomViewSet)
router.register('prices', CarPriceRelationShowroomViewSet)

urlpatterns = []
urlpatterns += router.urls
