from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_jwt.views import (obtain_jwt_token, refresh_jwt_token, verify_jwt_token)

from profiles.routers import router as profile_router
from office.routers import router as office_router
from journal.routers import router as journal_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('api/v1/', include(journal_router.urls)),  # Journal routers
    path('api/v1/', include(profile_router.urls)),  # Profiles routers
    path('api/v1/', include('office.urls')),  # Additionals for Office routers
    path('api/v1/', include(office_router.urls)),  # Office routers
    path('api/v1/', include('news.urls')),  # News routers
    path('api/v1/', include('journal.urls')),  # Journal routers

    path('auth/jwt/create/', obtain_jwt_token),  # Create auth token
    path('auth/jwt/refresh/', refresh_jwt_token),  # Verify auth token
    path('auth/jwt/verify/', verify_jwt_token),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
