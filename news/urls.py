from django.urls import path
from .views import NewsListAPIView, NewsDetailAPIView

urlpatterns: list = [
    path('news/<int:pk>/', NewsDetailAPIView.as_view()),
    path('news/', NewsListAPIView.as_view()),
]
