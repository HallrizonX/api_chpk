import os
from functools import wraps

from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

from rest_framework.response import Response
from rest_framework import status as st

from profiles.models import Profile


def file_cleanup(sender, **kwargs):
    """ Remove file from folder"""
    instance = kwargs['instance']

    try:
        file_path = instance.file.path
    except AttributeError:
        try:
            file_path = instance.image.path
        except AttributeError:
            file_path = instance.preview_image.path

    if os.path.exists(file_path):
        try:
            os.remove(file_path)
        except Exception as e:
            print(e)


def change_profile_from_teacher(sender, **kwargs):
    """ Update Profile and set [access=teacher] when creating new Teacher"""
    instance = kwargs['instance']
    profile = Profile.objects.get(id=instance.profile.id)
    profile.access = 'teacher'
    profile.save()


def bad_request(fnc):
    """ Error handler"""
    @wraps(fnc)
    def inner(request, *args, **kwargs):
        try:
            return fnc(request, *args, **kwargs)
        except ObjectDoesNotExist:
            return Response({'message': 'Object does not exist'}, status=st.HTTP_400_BAD_REQUEST)
        except MultipleObjectsReturned:
            return Response({'message': 'Get more then one object'}, status=st.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message': 'Are you sure in your action? Something wrong!'}, status=st.HTTP_423_LOCKED)
    return inner
