from django.contrib import admin
from profiles.models import Profile
from .models import (Group, Subject, Files, Teacher)


class SubjectAdmin(admin.ModelAdmin):

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

    def get_queryset(self, request):
        """ Get all marks for current profile"""
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            if request.user.is_superuser:
                return Files.objects.all()

        if profile.access == 'teacher':
            return Files.objects.filter(teachers__profile__user=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """ Set default teacher"""
        if db_field.name == 'subject':
            kwargs["queryset"] = Subject.objects.filter(teacher__profile__user=request.user)
            kwargs['initial'] = request.user.id
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Group)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Files, FilesAdmin)
admin.site.register(Teacher)
