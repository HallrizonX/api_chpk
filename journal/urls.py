from django.urls import path
from journal.views import RatingAPIView, RatingGroupAPIView, RatingCurrentStudentAPIView, RatingTeacherStudentAPIView

urlpatterns: list = [
    path('teacher/journals/', RatingTeacherStudentAPIView.as_view()),
    path('student/journals/', RatingCurrentStudentAPIView.as_view()),
    path('journals/<str:group_number>/groups/', RatingGroupAPIView.as_view()),
    path('journals/<str:pk>/', RatingAPIView.as_view()),
    path('journals/', RatingAPIView.as_view()),
]
