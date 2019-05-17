from .views import ProfileViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)

urlpatterns = router.urls