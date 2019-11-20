from rest_framework import routers

from .viewsets import PhoneViewSet

router = routers.SimpleRouter()
router.register('phones', PhoneViewSet)

urlpatterns = router.urls
