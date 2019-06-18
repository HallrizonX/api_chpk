from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status as st

from profiles.models import Profile
from profiles.serializers import ProfileSerializers

from office.serializers import TeacherSerializers, GroupSubjectSerializers, FilesTeacherSerializer, \
    SubjectTeacherSerializers
from office.models import Teacher, Group, Files, Subject
from office.mixins import ReadOnlyModelMixinViewSet

from utils import bad_request
from utils.CustomErrors import AccessError


class OfficeAPIView(APIView):
    """ Get current profile by token and return serializers data either teacher or student"""

    @bad_request
    @method_decorator(cache_page(settings.CACHE_TTL))
    def get(self, request) -> Response:
        user = Profile.objects.get(user=request.user)
        return Response({'result': self.get_office(user)}, status=st.HTTP_200_OK)

    @bad_request
    def get_office(self, user):
        if user.access == 'teacher':
            user = Teacher.objects.get(profile=user)
            serializer = TeacherSerializers(user)
        elif user.access == 'student':
            serializer = ProfileSerializers(user)

        return serializer.data
