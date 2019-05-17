from .views import TeacherViewSet, GroupViewSet, TeacherFilesViewSet, SubjectViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'teachers/files', TeacherFilesViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'subjects', SubjectViewSet)


urlpatterns = router.urls