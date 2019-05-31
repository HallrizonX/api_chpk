from rest_framework import permissions
from office.models import Teacher


class TeacherPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in ['GET']:
            return True
        else:
            try:
                teachers = Teacher.objects.get(profile__user=request.user)
            except Teacher.DoesNotExist:
                return False
            return teachers
