from django.contrib import admin

from profiles.models import Profile
from office.models import Subject

from journal.admin_tools.filters import TeacherSubjectsListFilter, JournalsSubjectListFilter
from journal.models import Student, Mark, Rating


class MarksAdmin(admin.ModelAdmin):
    list_display = ('date', 'mark')

    list_filter = (TeacherSubjectsListFilter,)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """ Set default teacher"""
        if db_field.name == 'author':
            kwargs['initial'] = request.user.id
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_queryset(self, request):
        """ Get all marks for current profile"""
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            if request.user.is_superuser:
                return Mark.objects.all()

        if profile.access == 'teacher':
            return Mark.objects.filter(author=request.user)

        if profile.access == 'student':
            return Mark.objects.filter(rating__student__profile=profile)


class RatingAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject')
    search_fields = ('student__profile__name', 'student__profile__surname', 'student__profile__last_name',
                     'subject__name', 'subject__group__number')
    list_filter = (JournalsSubjectListFilter,)
    filter_horizontal = ('marks',)

    def get_queryset(self, request):
        """ Get all marks for current profile"""
        try:
            profile = Profile.objects.get(user=request.user)
        except Profile.DoesNotExist:
            if request.user.is_superuser:
                return Rating.objects.all()

        if profile.access == 'teacher':
            return Rating.objects.filter(subject__teacher__profile_id=profile.id)
        if profile.access == 'student':
            return Rating.objects.filter(student__profile=profile)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """ Set default teacher"""
        if db_field.name == 'subject':
            if request.user.is_superuser:
                return super().formfield_for_foreignkey(db_field, request, **kwargs)

            kwargs["queryset"] = Subject.objects.filter(teacher__profile__user=request.user)
            kwargs['initial'] = request.user.id
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "marks" and request.method == 'GET':
            try:
                rating_id = request.META['PATH_INFO'].split('/')[-3]
                rating = Rating.objects.get(id=rating_id)
                kwargs["queryset"] = Mark.objects.filter(rating__student__id=rating.student.id,
                                                         rating__marks__author=request.user.id)
            except Exception:
                return super().formfield_for_manytomany(db_field, request, **kwargs)

        return super().formfield_for_manytomany(db_field, request, **kwargs)

    class Media:
        js = ("admin.js",)


admin.site.register(Rating, RatingAdmin)
admin.site.register(Mark, MarksAdmin)
admin.site.register(Student)
