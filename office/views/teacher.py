from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status as st

from office.serializers import (TeacherSerializers, FilesTeacherSerializer, SubjectFilesSerializer, GroupSubjectSerializers)
from office.models import Teacher, Files, Group
from profiles.models import Profile
from office.mixins import ReadOnlyModelMixinViewSet


class TeacherFilesAPIView(APIView):
    @method_decorator(cache_page(settings.CACHE_TTL))
    def get(self, request, pk) -> Response:
        queryset = Files.objects.filter(subject__teacher=pk)
        serializer = SubjectFilesSerializer(queryset, many=True)
        return Response({'result': serializer.data}, status=st.HTTP_200_OK)


class TeacherGroupsAPIView(APIView):
    @method_decorator(cache_page(settings.CACHE_TTL))
    def get(self, request) -> Response:
        queryset = Group.objects.filter(teachers__profile__user=request.user)
        serializer = GroupSubjectSerializers(queryset, many=True)
        return Response({'result': serializer.data}, status=st.HTTP_200_OK)

class TeacherFilesViewSet(ModelViewSet):
    queryset = Files.objects.all()
    serializer_class = FilesTeacherSerializer

    @method_decorator(cache_page(settings.CACHE_TTL))
    def list(self, request, *args, **kwargs) -> Response:
        """ Get all files for current teacher"""
        user_id = request.user.id
        queryset = Files.objects.filter(teachers__profile__user_id=user_id)
        serializer = FilesTeacherSerializer(queryset, many=True)

        return Response({'result': serializer.data})

    @method_decorator(cache_page(settings.CACHE_TTL))
    def retrieve(self, request, *args, **kwargs) -> Response:

        user_id = request.user.id

        try:
            queryset = Files.objects.filter(teachers__profile__user_id=user_id).get(pk=kwargs.get('pk'))
        except ObjectDoesNotExist:
            return Response(data={'msg': 'File with id={} does not exists'.format(kwargs.get('pk'))},
                            status=st.HTTP_400_BAD_REQUEST)

        serializer = FilesTeacherSerializer(queryset)
        return Response({'result': serializer.data}, status=st.HTTP_200_OK)


class TeacherViewSet(ReadOnlyModelMixinViewSet):
    model = Teacher
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializers
