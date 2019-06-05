from django.conf import settings
from rest_framework import serializers

from office.serializers import SubjectTeacherSerializers, SubjectFilesSerializer, ProfileSerializers

from journal.models import Mark, Student, Rating


class StudentSerializers(serializers.ModelSerializer):
    profile = ProfileSerializers()

    class Meta:
        model = Student
        fields: tuple = ('id', 'profile')


class MarkSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields: tuple = ('id', 'mark', 'date')


class DetailRatingSerializers(serializers.ModelSerializer):
    """ Serializer for detail journal, that can be filter pk and get current journal"""
    subject = SubjectTeacherSerializers()
    marks = MarkSerializers(many=True)

    class Meta:
        model = Rating
        fields: tuple = ('id', 'student', 'subject', 'marks',)


class ListRatingSerializers(serializers.ModelSerializer):
    """ Serializer which get list of journals"""
    student = StudentSerializers()
    detail_journal = serializers.SerializerMethodField(read_only=True)

    def get_detail_journal(self, obj):
        return f'{settings.API_VERSION_URL}journals/{obj.id}/'

    class Meta:
        model = Rating
        fields: tuple = ('detail_journal', 'id', 'student',)
