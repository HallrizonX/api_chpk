from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework import status as st
from rest_framework import permissions

from django.core.exceptions import ObjectDoesNotExist

from .models import Teacher, Group, Files, Subject
from .serializers import TeacherSerializers, GroupSubjectSerializers, FilesTeacherSerializer, SubjectTeacherSerializers


class TeacherFilesViewSet(ModelViewSet):
    permission_classes = (permissions.AllowAny,)  # Test permission
    queryset = Files.objects.all()
    serializer_class = FilesTeacherSerializer

    def list(self, request, *args, **kwargs):
        user_id = request.user.id
        queryset = Files.objects.filter(teacher__profile__user_id=user_id)
        serializer = FilesTeacherSerializer(queryset, many=True)

        return Response({'result': serializer.data})

    def retrieve(self, request, *args, **kwargs):
        user_id = request.user.id

        try:
            queryset = Files.objects.filter(teacher__profile__user_id=user_id).get(pk=kwargs.get('pk'))
        except ObjectDoesNotExist:
            return Response(data={'msg': 'File with id={} does not exists'.format(kwargs.get('pk'))},
                            status=st.HTTP_400_BAD_REQUEST)

        serializer = FilesTeacherSerializer(queryset)
        return Response({'result': serializer.data}, status=st.HTTP_200_OK)


class TeacherViewSet(ReadOnlyModelViewSet):
    permission_classes = (permissions.AllowAny,)  # Test permission
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializers

    def list(self, request, *args, **kwargs):
        serializer = TeacherSerializers(self.get_queryset(), many=True)
        return Response({'result': serializer.data}, status=st.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        queryset = Teacher.objects.get(pk=kwargs.get('pk'))
        serializer = TeacherSerializers(queryset)
        return Response({'result': serializer.data}, status=st.HTTP_200_OK)


class GroupViewSet(ReadOnlyModelViewSet):
    permission_classes = (permissions.AllowAny,)  # Test permission
    queryset = Group.objects.all()
    serializer_class = GroupSubjectSerializers

    def list(self, request, *args, **kwargs):
        serializer = GroupSubjectSerializers(self.get_queryset(), many=True)
        return Response({'result': serializer.data}, status=st.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        queryset = Group.objects.get(pk=kwargs.get('pk'))
        serializer = GroupSubjectSerializers(queryset)

        return Response({'result': serializer.data}, status=st.HTTP_200_OK)


class SubjectViewSet(ReadOnlyModelViewSet):
    permission_classes = (permissions.AllowAny,)  # Test permission
    queryset = Subject.objects.all()
    serializer_class = SubjectTeacherSerializers

    def list(self, request, *args, **kwargs):
        serializer = SubjectTeacherSerializers(self.get_queryset(), many=True)
        return Response({'result': serializer.data}, status=st.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        queryset = Subject.objects.get(pk=kwargs.get('pk'))
        serializer = SubjectTeacherSerializers(queryset)

        return Response({'result': serializer.data}, status=st.HTTP_200_OK)
