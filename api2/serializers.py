from rest_framework import serializers
from office.models import Teacher, Subject, Group, Files
from profiles.serializers import ProfileSerializers, SimpleProfileSerializers
from django.conf import settings
from office.serializers import SubjectTeacherSerializers, FilesSerializer
from journal.models import Rating
from journal.serializers import MarkSerializers
from .models import AdditionalFiles


class TeacherSerializers(serializers.ModelSerializer):
    profile = ProfileSerializers()

    class Meta:
        model = Teacher
        fields: tuple = ('id', 'profile')


class AdditionalFilesSerializers(serializers.ModelSerializer):

    class Meta:
        model = AdditionalFiles
        fields: tuple = ('id', 'file', 'title', 'pub_date')


class SubjectSerializers(serializers.ModelSerializer):
    detail_journal = serializers.SerializerMethodField(read_only=True)
    files = serializers.SerializerMethodField(read_only=True)
    teachers = serializers.SerializerMethodField(read_only=True)
    group = serializers.SerializerMethodField(read_only=True)
    additional_files = serializers.SerializerMethodField(read_only=True)

    def get_additional_files(self, obj):
        queryset = AdditionalFiles.objects.filter(group__number=obj.group.number)
        serializer = AdditionalFilesSerializers(queryset, many=True)

        return serializer.data

    def get_group(self, obj):
        return obj.group.number

    def get_teachers(self, obj):
        ser = TeacherSerializers(Teacher.objects.filter(subjects=obj), many=True)
        return ser.data

    def get_files(self, obj):
        ser = FilesSerializer(Files.objects.filter(subject_id=obj.id), many=True)
        return ser.data

    def get_detail_journal(self, obj):
        return f'/api/v2/journals/subjects/{obj.id}/'

    class Meta:
        model = Subject
        fields: tuple = ('id', 'name','group', 'detail_journal', 'files', 'teachers', 'additional_files')


class GroupListSerializers(serializers.ModelSerializer):
    teachers = TeacherSerializers(many=True)
    subject_set = SubjectSerializers(many=True)
    additional_files = serializers.SerializerMethodField(read_only=True)

    def get_additional_files(self, obj):
        queryset = AdditionalFiles.objects.filter(group__number=obj.number)
        serializer = AdditionalFilesSerializers(queryset, many=True)

        return serializer.data

    class Meta:
        model = Group
        fields: tuple = ('id', 'number', 'teachers', 'subject_set', 'additional_files')


class JournalSerializers(serializers.ModelSerializer):
    marks = MarkSerializers(many=True)
    class Meta:
        model = Rating
        fields: tuple = ('id', 'marks')