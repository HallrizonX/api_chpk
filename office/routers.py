from .views import (TeacherViewSet, GroupViewSet, GroupTeacherViewSet, TeacherFilesViewSet, SubjectViewSet,
                    GroupSubjectViewSet, SubjectTeacherViewSet)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'teachers/files', TeacherFilesViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'groups/teachers', GroupTeacherViewSet)
router.register(r'groups/subjects', GroupSubjectViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'subjects/teachers', SubjectTeacherViewSet)
router.register(r'subjects', SubjectViewSet)

urlpatterns = router.urls
