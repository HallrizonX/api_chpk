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
from rest_framework.viewsets import ReadOnlyModelViewSet
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

        profile = Profile.objects.get(user=request.user)

        if profile.access == 'student':
            queryset = Subject.objects.filter(group__number=kwargs.get('group_number'), group=profile.student.groups.id)
            if len(queryset) == 0:
                queryset = Subject.objects.filter(group__id=kwargs.get('group_number'), group=profile.student.groups.id)
        else:
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
        profile = Profile.objects.get(user=request.user)

        if profile.access == 'student':
            queryset = Teacher.objects.filter(subjects__group__number=kwargs.get('group_number'),
                                              subjects__group=profile.student.groups.id)
            if len(queryset) == 0:
                queryset = Teacher.objects.filter(subjects__group__id=kwargs.get('group_number'),
                                                  subjects__group__in=profile.student.groups)
        else:
            queryset = Teacher.objects.filter(subjects__group__number=kwargs.get('group_number'))
            if len(queryset) == 0:
                queryset = Teacher.objects.filter(subjects__group__id=kwargs.get('group_number'))

        serializer = TeacherSerializers(queryset, many=True)

        return Response({'result': serializer.data}, status=st.HTTP_200_OK)


class GroupViewSet(ReadOnlyModelViewSet):
    """ Get serializers data for group model"""
    queryset = Group.objects.all()
    serializer_class = GroupSubjectSerializers

    @bad_request
    @method_decorator(cache_page(settings.CACHE_TTL))
    def list(self, request, *args, **kwargs) -> Response:
        profile = Profile.objects.get(user=request.user)

        if profile.access == 'student':
            self.queryset = Group.objects.filter(student__profile=profile)

        serializer = self.serializer_class(self.queryset, many=True)
        return Response({'result': serializer.data}, status=st.HTTP_200_OK)

    @bad_request
    @method_decorator(cache_page(settings.CACHE_TTL))
    def retrieve(self, request, *args, **kwargs) -> Response:
        profile = Profile.objects.get(user=request.user)

        if profile.access == 'student':
            self.queryset = Group.objects.objects.get(pk=kwargs.get('pk'), student__profile=profile)
        else:
            self.queryset = Group.objects.objects.get(pk=kwargs.get('pk'))

        serializer = self.serializer_class(self.queryset)
        return Response({'result': serializer.data}, status=st.HTTP_200_OK)
