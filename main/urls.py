from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_jwt.views import (obtain_jwt_token, refresh_jwt_token, verify_jwt_token)

from profiles.routers import router as profile_router
from office.routers import router as office_router

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include(profile_router.urls)),
    path('api/v1/', include(office_router.urls)),
    path('api/v1/', include('news.urls')),

    path('auth/jwt/create/', obtain_jwt_token),
    path('auth/jwt/refresh/', refresh_jwt_token),
    path('auth/jwt/verify/', verify_jwt_token),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
