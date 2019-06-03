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


class GroupSubjectsAPIView(APIView):
    """ Get all subjects filter by group number """

    @bad_request
    @method_decorator(cache_page(settings.CACHE_TTL))
    def get(self, request, **kwargs) -> Response:
        queryset = Subject.objects.filter(group__number=kwargs.get('group_number'))

        if len(queryset) == 0:
            queryset = Subject.objects.filter(group__id=kwargs.get('group_number'))

        serializer = SubjectTeacherSerializers(queryset, many=True)

        return Response({'result': serializer.data})


class GroupTeachersAPIView(APIView):
    """ Get all teachers filter by group number """

    @bad_request
    @method_decorator(cache_page(settings.CACHE_TTL))
    def get(self, request, **kwargs) -> Response:
        queryset = Teacher.objects.filter(subjects__group__number=kwargs.get('group_number'))
        if len(queryset) == 0:
            queryset = Teacher.objects.filter(subjects__group__id=kwargs.get('group_number'))

        serializer = TeacherSerializers(queryset, many=True)

        return Response({'result': serializer.data}, status=st.HTTP_200_OK)


class GroupViewSet(ReadOnlyModelMixinViewSet):
    model = Group
    queryset = Group.objects.all()
    serializer_class = GroupSubjectSerializers
