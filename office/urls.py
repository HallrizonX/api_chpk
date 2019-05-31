from django.urls import path
from .views import (GroupTeachersAPIView, GroupSubjectsAPIView, SubjectTeachersAPIView, OfficeAPIView,
                    SubjectFilesAPIView, TeacherFilesAPIView, SubjectDetailFilesAPIView, SubjectStudentsAPIView
                    )

urlpatterns: list = [

    path('teachers/<str:pk>/files/', TeacherFilesAPIView.as_view()),
    path('groups/<str:group_number>/teachers/', GroupTeachersAPIView.as_view()),
    path('groups/<str:group_number>/subjects/', GroupSubjectsAPIView.as_view()),
    path('subjects/<str:pk>/teachers/', SubjectTeachersAPIView.as_view()),
    path('subjects/<str:pk>/files/', SubjectFilesAPIView.as_view()),
    path('subjects/<str:pk>/students/', SubjectStudentsAPIView.as_view()),
    path('subjects/<str:pk>/files/<str:pk_file>/', SubjectDetailFilesAPIView.as_view()),
    path('office/', OfficeAPIView.as_view()),
]
