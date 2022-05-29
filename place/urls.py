from .views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("places", UserViewSet)

urlpatterns = router.urls
