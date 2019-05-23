from django.core.exceptions import ObjectDoesNotExist

from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework import status as st

from profiles.models import Profile
from profiles.serializers import ProfileSerializers

from .serializers import TeacherSerializers, GroupSubjectSerializers, FilesTeacherSerializer, SubjectTeacherSerializers
from .models import Teacher, Group, Files, Subject
from .mixins import ReadOnlyModelMixinViewSet


class OfficeAPIView(APIView):
    """ Get all teachers filter by group number """

    def get(self, request) -> Response:
        user = Profile.objects.get(user=request.user)

        return Response({'result': self.get_office(user)}, status=st.HTTP_200_OK)

    def get_office(self, user):
        if user.access == 'teacher':
            user = Teacher.objects.get(profile=user)
            serializer = TeacherSerializers(user)
        elif user.access == 'student':
            serializer = ProfileSerializers(user)
        return serializer.data


class GroupSubjectsAPIView(APIView):
    """ Get all subjects filter by group number """

    def get(self, request, group_number) -> Response:
        queryset = Subject.objects.filter(group__number=group_number)
        serializer = SubjectTeacherSerializers(queryset, many=True)

        return Response({'result': serializer.data})


class GroupTeachersAPIView(APIView):
    """ Get all teachers filter by group number """

    def get(self, request, group_number) -> Response:
        queryset = Teacher.objects.filter(subjects__group__number=group_number)
        serializer = TeacherSerializers(queryset, many=True)

        return Response({'result': serializer.data}, status=st.HTTP_200_OK)


class GroupSubjectsAPIView(APIView):
    """ Get all subjects filter by group number """

    def get(self, request, group_number) -> Response:
        queryset = Subject.objects.filter(group__number=group_number)
        serializer = SubjectTeacherSerializers(queryset, many=True)

        return Response({'result': serializer.data})


class SubjectTeachersAPIView(APIView):
    def get(self, request, pk) -> Response:
        queryset = Teacher.objects.filter(subjects__id=pk)
        serializer = TeacherSerializers(queryset, many=True)

        return Response({'result': serializer.data}, status=st.HTTP_200_OK)


class TeacherFilesViewSet(ModelViewSet):
    queryset = Files.objects.all()
    serializer_class = FilesTeacherSerializer

    def list(self, request, *args, **kwargs) -> Response:
        """ Get all files for current teacher"""
        user_id = request.user.id
        queryset = Files.objects.filter(teacher__profile__user_id=user_id)
        serializer = FilesTeacherSerializer(queryset, many=True)

        return Response({'result': serializer.data})

    def retrieve(self, request, *args, **kwargs) -> Response:
        user_id = request.user.id

        try:
            queryset = Files.objects.filter(teacher__profile__user_id=user_id).get(pk=kwargs.get('pk'))
        except ObjectDoesNotExist:
            return Response(data={'msg': 'File with id={} does not exists'.format(kwargs.get('pk'))},
                            status=st.HTTP_400_BAD_REQUEST)

        serializer = FilesTeacherSerializer(queryset)
        return Response({'result': serializer.data}, status=st.HTTP_200_OK)


class TeacherViewSet(ReadOnlyModelMixinViewSet):
    model = Teacher
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializers


class GroupViewSet(ReadOnlyModelMixinViewSet):
    model = Group
    queryset = Group.objects.all()
    serializer_class = GroupSubjectSerializers


class SubjectViewSet(ReadOnlyModelMixinViewSet):
    model = Subject
    queryset = Subject.objects.all()
    serializer_class = SubjectTeacherSerializers
