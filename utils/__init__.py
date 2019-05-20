from profiles.models import Profile
import os


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
