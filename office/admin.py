from django.contrib import admin
from .models import (Group, Subject, Files, Teacher)

admin.site.register(Group)
admin.site.register(Subject)
admin.site.register(Files)
admin.site.register(Teacher)

