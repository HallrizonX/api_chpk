from rest_framework import serializers
from .models import Teacher, Subject, Group, Files
from profiles.serializers import ProfileSerializers


class GroupSubjectSerializers(serializers.ModelSerializer):
    """Serializer Group table for Subject"""

    class Meta:
        model = Group
        fields: tuple = ('id', 'number')


class SubjectTeacherSerializers(serializers.ModelSerializer):
    """Serializer Subject table for Teacher and Files"""
    group = GroupSubjectSerializers()

    class Meta:
        model = Subject
        fields: tuple = ('id', 'name', 'group',)


class FilesTeacherSerializer(serializers.ModelSerializer):
    subject = SubjectTeacherSerializers()

    class Meta:
        model = Files
        fields: tuple = ('id', 'file', 'title', 'subject')


class TeacherSerializers(serializers.ModelSerializer):
    """Serializer Teacher table"""
    profile = ProfileSerializers()
    subjects = SubjectTeacherSerializers(many=True)
    files = FilesTeacherSerializer(many=True)

    class Meta:
        model = Teacher
        fields: tuple = ('id', 'profile', 'subjects', 'files')
