from django.urls import path
from .views import GroupAPIView, JournalAPIView, FeedbackAPIView

urlpatterns: list = [
    path('groups/', GroupAPIView.as_view()),
    path('feedback/', FeedbackAPIView.as_view()),
    path('journals/subjects/<str:subject_id>/', JournalAPIView.as_view())
]
