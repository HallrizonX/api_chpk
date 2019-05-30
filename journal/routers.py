from journal.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'marks', MarkViewSet)

urlpatterns = router.urls
