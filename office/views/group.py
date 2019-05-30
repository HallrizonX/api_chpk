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

from office.serializers import TeacherSerializers, GroupSubjectSerializers, FilesTeacherSerializer, SubjectTeacherSerializers
from office.models import Teacher, Group, Files, Subject
from office.mixins import ReadOnlyModelMixinViewSet


class GroupSubjectsAPIView(APIView):
    """ Get all subjects filter by group number """

    @method_decorator(cache_page(settings.CACHE_TTL))
    def get(self, request, group_number) -> Response:
        queryset = Subject.objects.filter(group__number=group_number)
        serializer = SubjectTeacherSerializers(queryset, many=True)

        return Response({'result': serializer.data})


class GroupTeachersAPIView(APIView):
    """ Get all teachers filter by group number """

    @method_decorator(cache_page(settings.CACHE_TTL))
    def get(self, request, group_number) -> Response:
        queryset = Teacher.objects.filter(subjects__group__number=group_number)
        serializer = TeacherSerializers(queryset, many=True)

        return Response({'result': serializer.data}, status=st.HTTP_200_OK)


class GroupSubjectsAPIView(APIView):
    """ Get all subjects filter by group number """

    @method_decorator(cache_page(settings.CACHE_TTL))
    def get(self, request, group_number) -> Response:
        queryset = Subject.objects.filter(group__number=group_number)
        serializer = SubjectTeacherSerializers(queryset, many=True)

        return Response({'result': serializer.data})




class GroupViewSet(ReadOnlyModelMixinViewSet):
    model = Group
    queryset = Group.objects.all()
    serializer_class = GroupSubjectSerializers

