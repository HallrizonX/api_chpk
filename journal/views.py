from django.shortcuts import render

from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from rest_framework.response import Response
from rest_framework import status as st

from journal.models import Rating, Mark, Student
from journal.serializers import ListRatingSerializers, DetailRatingSerializers, MarkSerializers

from journal.permissions import TeacherPermission


class RatingAPIView(APIView):
    """ Get either list journals or detail journal """

    def get(self, request, **kwargs) -> Response:

        if kwargs.get('pk') is None:
            ratings = Rating.objects.all()
            serializer = ListRatingSerializers(ratings, many=True)
        else:
            rating = Rating.objects.get(id=kwargs.get('pk'))
            serializer = DetailRatingSerializers(rating)

        return Response({'result': serializer.data}, status=st.HTTP_200_OK)


class RatingGroupAPIView(APIView):
    """ Get list of journal filtered by group number"""

    def get(self, request, group_number) -> Response:
        ratings = Rating.objects.filter(subject__group__number=group_number)
        serializer = ListRatingSerializers(ratings, many=True)

        return Response({'result': serializer.data}, status=st.HTTP_200_OK)


class RatingCurrentStudentAPIView(APIView):
    """ Get list of journal for current student"""

    def get(self, request) -> Response:
        ratings = Rating.objects.filter(student__profile__user=request.user)
        serializer = ListRatingSerializers(ratings, many=True)

        return Response({'result': serializer.data}, status=st.HTTP_200_OK)


class RatingTeacherStudentAPIView(APIView):
    """ Get list of journal for current teacher"""

    def get(self, request) -> Response:
        ratings = Rating.objects.filter(subject__teacher__profile__user=request.user)
        serializer = ListRatingSerializers(ratings, many=True)

        return Response({'result': serializer.data}, status=st.HTTP_200_OK)


class MarkViewSet(ModelViewSet):
    """ Work with marks"""
    serializer_class = MarkSerializers
    queryset = Mark.objects.all()
    permission_classes = (TeacherPermission,)
