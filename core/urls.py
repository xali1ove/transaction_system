from rest_framework import routers
from .views import ClientViewSet


router = routers.SimpleRouter(trailing_slash=False)
router.register(r"client", ClientViewSet, basename='client')

urlpatterns = router.urls
