from django.urls import path
from .views import GroupTeachersAPIView, GroupSubjectsAPIView, SubjectTeachersAPIView

urlpatterns: list = [
    path('groups/<str:group_number>/teachers/', GroupTeachersAPIView.as_view()),
    path('groups/<str:group_number>/subjects/', GroupSubjectsAPIView.as_view()),
    path('subjects/<str:pk>/teachers/', SubjectTeachersAPIView.as_view())
]
