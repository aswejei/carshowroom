from rest_framework.routers import DefaultRouter

from serv.carshowroom.views import CarShowroomViewSet, CarPriceRelationShowroomViewSet, CustomerShowroomOfferViewSet

router = DefaultRouter()
router.register('carshowrooms', CarShowroomViewSet)
router.register('prices', CarPriceRelationShowroomViewSet)
router.register('offers', CustomerShowroomOfferViewSet, basename='CustomerShowroomOffers')

urlpatterns = []
urlpatterns += router.urls
