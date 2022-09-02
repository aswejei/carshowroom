from rest_framework.routers import SimpleRouter

from carshowroom.views import CarShowroomViewSet, CarPriceRelationShowroomViewSet

router = SimpleRouter()
router.register('', CarShowroomViewSet)
router.register('prices', CarPriceRelationShowroomViewSet)

urlpatterns = []
urlpatterns += router.urls
