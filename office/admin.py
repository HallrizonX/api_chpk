from django.contrib import admin

from profiles.models import Profile
from journal.admin_tools.filters import FilesSubjectListFilter
from .models import (Group, Subject, Files, Teacher)


class ModelFilesInline(admin.StackedInline):
    model = Files

    def get_queryset(self, request):
        """ Get all marks for current profile"""
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            if request.user.is_superuser:
                return Files.objects.all()

        if profile.access == 'teacher':
            return Files.objects.filter(subject__teacher__profile=profile)


class SubjectAdmin(admin.ModelAdmin):
    inlines = [ModelFilesInline]
    search_fields = ('group__number', 'name')

    def get_queryset(self, request):
        """ Get all marks for current profile"""
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            if request.user.is_superuser:
                return Subject.objects.all()

        if profile.access == 'teacher':
            return Subject.objects.filter(teacher__profile_id=profile.id)


class FilesAdmin(admin.ModelAdmin):
    list_filter = (FilesSubjectListFilter,)

    def get_queryset(self, request):
        """ Get all marks for current profile"""
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            if request.user.is_superuser:
                return Files.objects.all()

        if profile.access == 'teacher':
            return Files.objects.filter(subject__teacher__profile__user=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """ Set default teacher"""
        if db_field.name == 'subject' and request.method == 'GET':
            if request.user.is_superuser:
                kwargs["queryset"] = Subject.objects.all()
            else:
                kwargs["queryset"] = Subject.objects.filter(teacher__profile__user=request.user)
            kwargs['initial'] = request.user.id

        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class TeacherAdmin(admin.ModelAdmin):
    search_fields = ('profile__user__username', 'profile__name', 'profile__surname', 'profile__last_name')
    list_filter = ('groups', 'subjects',)


admin.site.register(Group)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Files, FilesAdmin)
admin.site.register(Teacher, TeacherAdmin)
