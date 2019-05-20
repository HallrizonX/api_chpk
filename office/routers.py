from .views import (TeacherViewSet, GroupViewSet, TeacherFilesViewSet, SubjectViewSet)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'teachers/files', TeacherFilesViewSet)  # Work with files in personal teacher office
router.register(r'teachers', TeacherViewSet)  # LIST/RETRIEVE
router.register(r'groups', GroupViewSet)  # LIST/RETRIEVE
router.register(r'subjects', SubjectViewSet)  # LIST/RETRIEVE

urlpatterns = router.urls
