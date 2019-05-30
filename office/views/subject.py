from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status as st

from office.serializers import TeacherSerializers, SubjectTeacherSerializers, SubjectFilesSerializer
from office.models import Teacher, Group, Files, Subject
from office.mixins import ReadOnlyModelMixinViewSet


class SubjectFilesAPIView(APIView):
    @method_decorator(cache_page(settings.CACHE_TTL))
    def get(self, request, pk) -> Response:
        queryset = Files.objects.filter(subject__id=pk)
        serializer = SubjectFilesSerializer(queryset, many=True)

        return Response({'result': serializer.data}, status=st.HTTP_200_OK)


class SubjectTeachersAPIView(APIView):
    @method_decorator(cache_page(settings.CACHE_TTL))
    def get(self, request, pk) -> Response:
        queryset = Teacher.objects.filter(subjects__id=pk)
        serializer = TeacherSerializers(queryset, many=True)

        return Response({'result': serializer.data}, status=st.HTTP_200_OK)


class SubjectViewSet(ReadOnlyModelMixinViewSet):
    model = Subject
    queryset = Subject.objects.all()
    serializer_class = SubjectTeacherSerializers
