from django.shortcuts import render

from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from rest_framework.response import Response
from rest_framework import status as st

from profiles.models import Profile
from journal.models import Rating, Mark, Student
from office.models import Group, Subject, Teacher
from office.serializers import SubjectTeacherSerializers

from journal.serializers import ListRatingSerializers, DetailRatingSerializers, MarkSerializers

from journal.permissions import TeacherPermission
from utils import bad_request


class RatingAPIView(APIView):
    """ Get either list journals or detail journal """

    @bad_request
    def get(self, request, **kwargs) -> Response:
        profile = Profile.objects.get(user=request.user)
        if kwargs.get('pk') is None:
            ratings = Rating.objects.filter(subject__teacher__profile=profile)
            serializer = ListRatingSerializers(ratings, many=True)
        else:
            rating = Rating.objects.get(id=str(kwargs.get('pk')), subject__teacher__profile=profile)
            serializer = DetailRatingSerializers(rating)

        return Response({'result': serializer.data}, status=st.HTTP_200_OK)

class RatingGroupAPIView(APIView):
    """ Get list of journal filtered by group number"""

    @bad_request
    def get(self, request, group_number) -> Response:
        ratings = Rating.objects.filter(subject__group__number=group_number)
        serializer = ListRatingSerializers(ratings, many=True)

        return Response({'result': serializer.data}, status=st.HTTP_200_OK)

class RatingCurrentStudentAPIView(APIView):
    """ Get list of journal for current student"""

    @bad_request
    def get(self, request) -> Response:
        ratings = Rating.objects.filter(student__profile__user=request.user)
        serializer = ListRatingSerializers(ratings, many=True)

        return Response({'result': serializer.data}, status=st.HTTP_200_OK)


class RatingTeacherAPIView(APIView):
    """ Get list of journal for current teacher"""
    permission_classes = (TeacherPermission,)

    @bad_request
    def get(self, request) -> Response:
        ratings = Rating.objects.filter(subject__teacher__profile__user=request.user)
        serializer = ListRatingSerializers(ratings, many=True)

        return Response({'result': serializer.data}, status=st.HTTP_200_OK)


class RatingTeacherSubjectInGroupAPIView(APIView):
    """ Get list of journals for current group where teacher existing"""
    permission_classes = (TeacherPermission,)

    @bad_request
    def get(self, request, group_number) -> Response:
        profile = Profile.objects.get(user=request.user)
        journals = Rating.objects.filter(subject__group__number=group_number, subject__teacher__profile=profile)
        serializer = ListRatingSerializers(journals, many=True)

        return Response({'result': serializer.data}, status=st.HTTP_200_OK)


class RatingTeacherGroupSubjectsAPIView(APIView):
    """ Get list of journals for current group where teacher existing"""
    permission_classes = (TeacherPermission,)

    @bad_request
    def get(self, request, group_number) -> Response:
        profile = Profile.objects.get(user=request.user)

        subjects = Subject.objects.filter(group__number=group_number, teacher__profile=profile)
        serializer = SubjectTeacherSerializers(subjects, many=True)

        return Response({'result': serializer.data}, status=st.HTTP_200_OK)


class RatingTeacherSubjectsAPIView(APIView):
    """ Get list of journals for current subject where teacher existing"""
    permission_classes = (TeacherPermission,)

    @bad_request
    def get(self, request, subject_id) -> Response:
        profile = Profile.objects.get(user=request.user)
        journals = Rating.objects.filter(subject_id=subject_id, subject__teacher__profile=profile)
        serializer = ListRatingSerializers(journals, many=True)

        return Response({'result': serializer.data}, status=st.HTTP_200_OK)


class MarkViewSet(ModelViewSet):
    """ Work with marks"""
    serializer_class = MarkSerializers
    queryset = Mark.objects.all()
    permission_classes = (TeacherPermission,)
