from django.conf import settings
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as st

from office.serializers import TeacherSerializers, SubjectTeacherSerializers, SubjectFilesSerializer
from office.models import Teacher, Files, Subject
from office.mixins import ReadOnlyModelMixinViewSet
from journal.models import Student, Rating
from journal.serializers import StudentSerializers

class SubjectStudentsAPIView(APIView):
    """ Get of student for current subject"""
    @method_decorator(cache_page(settings.CACHE_TTL))
    def get(self, request, pk) -> Response:
        queryset = Student.objects.filter(subjects__in=pk)
        serializer = StudentSerializers(queryset, many=True)

        return Response({'result': serializer.data}, status=st.HTTP_200_OK)

    def post(self, request, pk) -> Response:
        """ Create new file for teacher"""
        try:
            teacher = Teacher.objects.get(profile__user=request.user)
            file = Files.objects.create(title=request.data['title'], subject_id=pk, file=request.data['file'])
            teacher.files.add(file)
            teacher.save()
            serializer = SubjectFilesSerializer(Files.objects.get(id=file.id))
            return Response({'result': serializer.data}, status=st.HTTP_201_CREATED)
        except:
            return Response(status=st.HTTP_403_FORBIDDEN)

class SubjectFilesAPIView(APIView):
    """ Working with list of files for current subject"""
    @method_decorator(cache_page(settings.CACHE_TTL))
    def get(self, request, pk) -> Response:
        queryset = Files.objects.filter(subject__id=pk)
        serializer = SubjectFilesSerializer(queryset, many=True)

        return Response({'result': serializer.data}, status=st.HTTP_200_OK)

    def post(self, request, pk) -> Response:
        """ Create new file for teacher"""
        try:
            teacher = Teacher.objects.get(profile__user=request.user)
            file = Files.objects.create(title=request.data['title'], subject_id=pk, file=request.data['file'])
            teacher.files.add(file)
            teacher.save()
            serializer = SubjectFilesSerializer(Files.objects.get(id=file.id))
            return Response({'result': serializer.data}, status=st.HTTP_201_CREATED)
        except:
            return Response(status=st.HTTP_403_FORBIDDEN)


class SubjectDetailFilesAPIView(APIView):
    """ Working with current file"""
    @method_decorator(cache_page(settings.CACHE_TTL))
    def get(self, request, pk, pk_file):
        try:
            file = Files.objects.get(id=pk_file)
            serializer = SubjectFilesSerializer(file)
            return Response({'result': serializer.data}, status=st.HTTP_200_OK)
        except Files.DoesNotExist:
            return Response({f'File with id {pk_file} does not exist'}, status=st.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, pk_file) -> Response:
        file = Files.objects.get(id=pk_file)

        if request.data.get('title'):
            file.title = request.data['title']
            file.save()

        if request.data.get('file'):
            file.file = request.data['file']
            file.save()

        serializer = SubjectFilesSerializer(file)
        return Response({'result': serializer.data}, status=st.HTTP_200_OK)

    def put(self, request, pk, pk_file) -> Response:

        try:
            file = Files.objects.get(id=pk_file)
            file.file = request.data['file']
            file.title = request.data['title']
            file.save()
        except:
            return Response(status=st.HTTP_400_BAD_REQUEST)

        serializer = SubjectFilesSerializer(file)
        return Response({'result': serializer.data}, status=st.HTTP_200_OK)

    def delete(self, request, pk, pk_file) -> Response:
        file = Files.objects.get(id=pk_file)
        file.delete()
        return Response({'result': 'success'}, status=st.HTTP_200_OK)


class SubjectTeachersAPIView(APIView):
    """ Get list of teachers for current subject"""
    @method_decorator(cache_page(settings.CACHE_TTL))
    def get(self, request, pk) -> Response:
        queryset = Teacher.objects.filter(subjects__id=pk)
        serializer = TeacherSerializers(queryset, many=True)

        return Response({'result': serializer.data}, status=st.HTTP_200_OK)


class SubjectViewSet(ReadOnlyModelMixinViewSet):
    """ Working with subject either get list or get detail"""
    model = Subject
    queryset = Subject.objects.all()
    serializer_class = SubjectTeacherSerializers
