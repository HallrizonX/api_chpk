from profiles.models import Profile
import os


def file_cleanup(sender, **kwargs):
    """ Remove file from folder"""
    instance = kwargs['instance']
    if os.path.exists(instance.file.path):
        try:
            os.remove(instance.file.path)
        except Exception as e:
            print(e)


def change_profile_from_teacher(sender, **kwargs):
    """ Update Profile and set [access=teacher] when creating new Teacher"""
    instance = kwargs['instance']
    profile = Profile.objects.get(id=instance.profile.id)
    profile.access = 'teacher'
    profile.save()
