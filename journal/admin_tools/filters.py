from django.contrib import admin
from profiles.models import Profile
from office.models import Subject
from journal.models import Rating


class TeacherSubjectsListFilter(admin.SimpleListFilter):
    """ Filter by group number for marks admin panel"""
    title = 'предметами'
    parameter_name = 'subjects'
    default_value = None

    def lookups(self, request, model_admin):
        list_of_species = []
        if request.user.is_superuser:
            queryset = Subject.objects.all()
        else:
            queryset = Subject.objects.filter(rating__marks__author=request.user)

        for species in queryset:
            list_of_species.append(
                (str(species.id), f'{species.group.number} : {species.name}')
            )
        return sorted(list_of_species, key=lambda tp: tp[1])

    def queryset(self, request, queryset):
        if self.value() is not None:
            return queryset.filter(rating__subject_id=self.value())
        return queryset.all()

    def value(self):
        value = super().value()
        return value


class FilesSubjectListFilter(admin.SimpleListFilter):
    """ Filters for teacher files in admin panel"""
    title = 'предметами'
    parameter_name = 'subjects'
    default_value = None

    def lookups(self, request, model_admin):
        list_of_species = []
        if request.user.is_superuser:
            queryset = Subject.objects.all()
        else:
            queryset = Subject.objects.filter(teacher__profile__user=request.user)

        for species in queryset:
            print(species.group.number)
            list_of_species.append(
                (str(species.id), f'{species.group.number} : {species.name}')
            )
        return sorted(list_of_species, key=lambda tp: tp[1])

    def queryset(self, request, queryset):
        if self.value() is not None:
            return queryset.filter(subject__id=self.value())
        return queryset.all()

    def value(self):
        value = super().value()
        return value


class SubjectListFilter(admin.SimpleListFilter):
    """ Filters for teacher files in admin panel"""
    title = 'предметами'
    parameter_name = 'subjects'
    default_value = None

    def lookups(self, request, model_admin):
        list_of_species = []
        if request.user.is_superuser:
            queryset = Subject.objects.all()
        else:
            queryset = Subject.objects.filter(teacher__profile__user=request.user)

        for species in queryset:
            print(species.group.number)
            list_of_species.append(
                (str(species.id), f'{species.group.number} : {species.name}')
            )
        return sorted(list_of_species, key=lambda tp: tp[1])

    def queryset(self, request, queryset):
        if self.value() is not None:
            return queryset.filter(id=self.value())
        return queryset.all()

    def value(self):
        value = super().value()
        return value


class JournalsSubjectListFilter(admin.SimpleListFilter):
    """ Filters for teacher journals by subject in admin panel"""
    title = 'предметами'
    parameter_name = 'subjects'
    default_value = None

    def lookups(self, request, model_admin):
        list_of_species = []
        if request.user.is_superuser:
            queryset = Subject.objects.all()
        else:
            queryset = Subject.objects.filter(teacher__profile__user=request.user)

        for species in queryset:
            print(species.group.number)
            list_of_species.append(
                (str(species.id), f'{species.group.number} : {species.name}')
            )
        return sorted(list_of_species, key=lambda tp: tp[1])

    def queryset(self, request, queryset):
        if self.value() is not None:
            return queryset.filter(subject_id=self.value())
        return queryset.all()

    def value(self):
        value = super().value()
        return value
