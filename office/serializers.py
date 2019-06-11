from rest_framework import serializers
from .models import Teacher, Subject, Group, Files
from profiles.serializers import ProfileSerializers, SimpleProfileSerializers
from django.conf import settings


class GroupSubjectSerializers(serializers.ModelSerializer):
    """Serializer group table for subject"""
    group_subjects = serializers.SerializerMethodField(read_only=True)
    group_teachers = serializers.SerializerMethodField(read_only=True)

    def get_group_subjects(self, obj):
        return f'{settings.API_VERSION_URL}groups/{obj.number}/subjects/'

    def get_group_teachers(self, obj):
        return f'{settings.API_VERSION_URL}groups/{obj.number}/teachers/'

    class Meta:
        model = Group
        fields: tuple = ('group_subjects', 'group_teachers', 'id', 'number')


class SubjectTeacherSerializers(serializers.ModelSerializer):
    """Serializer Subject table for Teacher and Files"""
    group = GroupSubjectSerializers()

    subject_teachers = serializers.SerializerMethodField(read_only=True)
    subject_files = serializers.SerializerMethodField(read_only=True)

    def get_subject_teachers(self, obj):
        return f'{settings.API_VERSION_URL}subjects/{obj.id}/teachers/'

    def get_subject_files(self, obj):
        return f'{settings.API_VERSION_URL}subjects/{obj.id}/files/'

    class Meta:
        model = Subject
        fields: tuple = ('subject_teachers', 'subject_files', 'id', 'name', 'group',)


class FilesTeacherSerializer(serializers.ModelSerializer):
    """ Serializers all files for current teacher"""
    subject = SubjectTeacherSerializers()

    class Meta:
        model = Files
        fields: tuple = ('id', 'file', 'title', 'subject')

class FilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Files
        fields: tuple = ('id', 'file', 'title')


class TeacherSerializers(serializers.ModelSerializer):
    """Serializer teacher table"""
    profile = ProfileSerializers()
    subjects = SubjectTeacherSerializers(many=True)

    url_files = serializers.SerializerMethodField(read_only=True)

    def get_url_files(self, obj):
        return f'{settings.API_VERSION_URL}teachers/{obj.id}/files/'

    class Meta:
        model = Teacher
        fields: tuple = ('url_files', 'id', 'profile', 'subjects')


class SimpleTeacherSerializers(serializers.ModelSerializer):
    """Serializer teacher table for subjects file"""
    profile = SimpleProfileSerializers()

    class Meta:
        model = Teacher
        fields: tuple = ('id', 'profile')


class SubjectFilesSerializer(serializers.ModelSerializer):
    """ Serializers all files for current subject"""
    teachers = SimpleTeacherSerializers(many=True)

    class Meta:
        model = Files
        fields: tuple = ('id', 'file', 'title', 'teachers')
