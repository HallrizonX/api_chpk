from django.urls import path
from .views import GroupAPIView, JournalAPIView

urlpatterns: list = [
    path('groups/', GroupAPIView.as_view()),
    path('journals/subjects/<str:subject_id>/', JournalAPIView.as_view())
]
