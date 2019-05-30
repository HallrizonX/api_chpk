from django.contrib import admin
from journal.models import Student, Mark, Rating

admin.site.register(Student)
admin.site.register(Mark)


class RatingAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject')
    search_fields = ('student__profile__name', 'student__profile__surname', 'student__profile__last_name',
                     'subject__name', 'subject__group__number')
    list_filter = ('subject', 'student')

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "marks" and request.method == 'GET':
            try:
                rating_id = request.META['PATH_INFO'].split('/')[-3]
                rating = Rating.objects.get(id=rating_id)
                kwargs["queryset"] = Mark.objects.filter(rating__student__id=rating.student.id)
                print(kwargs["queryset"])
            except Exception:
                return super().formfield_for_manytomany(db_field, request, **kwargs)

        return super().formfield_for_manytomany(db_field, request, **kwargs)


admin.site.register(Rating, RatingAdmin)
