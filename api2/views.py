from django.shortcuts import render
from django.shortcuts import render

from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.viewsets import ModelViewSet

from rest_framework.response import Response
from rest_framework import status as st

from profiles.models import Profile
from journal.models import Rating, Mark, Student
from office.models import Group, Subject, Teacher
from office.serializers import SubjectTeacherSerializers, GroupSubjectSerializers
from .serializers import GroupListSerializers, JournalSerializers
from journal.serializers import ListRatingSerializers, DetailRatingSerializers, MarkSerializers
from .models import Feedback
from journal.permissions import TeacherPermission
from utils import bad_request


class UserProfile:
    access: str = ""
    profile = None

    def __init__(self, request):
        if request.user.is_anonymous:
            raise Profile.DoesNotExist('User is anonymous')

        self.profile = Profile.objects.get(user=request.user)
        self.access = self.profile.access

    @property
    def get_groups(self) -> Group:
        if self.access == 'teacher':
            return Group.objects.filter(teachers__profile=self.profile)
        elif self.access == 'student':
            return Group.objects.filter(student__profile=self.profile)

        raise Group.DoesNotExist("Groups don't exist")

    def get_journals_by_subject_id(self, subject_id) -> Rating:
        if self.access == 'teacher':
            return Rating.objects.filter(
                subject=Subject.objects.get(id=subject_id, subject__teacher__profile=self.profile))
        elif self.access == 'student':
            return Rating.objects.filter(student__profile=self.profile, subject=Subject.objects.get(id=subject_id))

        raise Rating.DoesNotExist("Journals don't exist")


class GroupAPIView(ListAPIView):
    serializer_class = GroupListSerializers

    def list(self, request, *args, **kwargs) -> Response:
        profile = UserProfile(request)
        serializer = self.serializer_class(profile.get_groups, many=True)
        return Response({'result': serializer.data}, status=st.HTTP_200_OK)


class JournalAPIView(ListAPIView):
    serializer_class = JournalSerializers

    def list(self, request, *args, **kwargs) -> Response:
        profile = UserProfile(request)
        subject_id = kwargs.get('subject_id')

        serializer = self.serializer_class(
            profile.get_journals_by_subject_id(subject_id), many=True
        )
        return Response({'result': serializer.data}, status=st.HTTP_200_OK)


class FeedbackAPIView(APIView):

    def post(self, request):
        profile = Profile.objects.get(user=request.user)
        Feedback.objects.create(
            author=profile,
            thema=request.data['thema'],
            message=request.data['message']
        )
        return Response({'result': 'fack'}, status=st.HTTP_200_OK)

