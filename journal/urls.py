from django.urls import path
from journal.views import (RatingAPIView, RatingGroupAPIView, RatingCurrentStudentAPIView, RatingTeacherAPIView,
                           RatingTeacherSubjectInGroupAPIView, RatingTeacherSubjectsAPIView, RatingTeacherGroupSubjectsAPIView)

urlpatterns: list = [
    path('teacher/journals/', RatingTeacherAPIView.as_view()),
    path('teacher/groups/<str:group_number>/subjects/', RatingTeacherGroupSubjectsAPIView.as_view()),
    path('teacher/groups/<str:group_number>/journals/', RatingTeacherSubjectInGroupAPIView.as_view()),
    path('teacher/subjects/<str:subject_id>/journals/', RatingTeacherSubjectsAPIView.as_view()),

    path('student/journals/', RatingCurrentStudentAPIView.as_view()),

    path('journals/<str:group_number>/groups/', RatingGroupAPIView.as_view()),

    path('journals/<str:pk>/marks/', RatingAPIView.as_view()),
    path('journals/<str:pk>/', RatingAPIView.as_view()),
    path('journals/', RatingAPIView.as_view()),
]
