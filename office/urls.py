from django.urls import path
from .views import (GroupTeachersAPIView, GroupSubjectsAPIView, SubjectTeachersAPIView, OfficeAPIView,
                    SubjectFilesAPIView, TeacherFilesAPIView
                    )

urlpatterns: list = [
    path('teachers/<str:pk>/files/', TeacherFilesAPIView.as_view()),
    path('groups/<str:group_number>/teachers/', GroupTeachersAPIView.as_view()),
    path('groups/<str:group_number>/subjects/', GroupSubjectsAPIView.as_view()),
    path('subjects/<str:pk>/teachers/', SubjectTeachersAPIView.as_view()),
    path('subjects/<str:pk>/files/', SubjectFilesAPIView.as_view()),
    path('office/', OfficeAPIView.as_view()),
]
