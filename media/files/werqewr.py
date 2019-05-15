from django.urls import path
from office.views import OfficeIndex

urlpatterns = [
    path("", OfficeIndex.as_view(), name="office_index")
]
