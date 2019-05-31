from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from django_summernote.models import Attachment
from .models import News, Image

admin.site.site_title = 'Адміністративна частина ЧПК'
admin.site.index_title = 'Адміністратор'
admin.site.site_header = 'ДВНЗ "Чернівецький політехнічний коледж"'
admin.site.unregister(Attachment)


class NewsAdmin(SummernoteModelAdmin):  # instead of ModelAdmin

    fieldsets = [
        (None, {'fields': ['title']}),
        ('Інформація', {'fields': ['short_description', 'description', ]}),
        ('Картинки', {'fields': ['preview_image', 'images']}),

    ]
    summernote_fields = '__all__'
    list_display = ("title", "pub_date", "short_description",)
    list_filter = ("pub_date",)


admin.site.register(News, NewsAdmin)
admin.site.register(Image)
