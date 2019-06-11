from django.db import models
from profiles.models import Profile
from office.models import Group
import datetime

class Feedback(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    thema = models.CharField(max_length=220)
    message = models.TextField()
    available = models.BooleanField(default=True, blank=True)
    pub_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f'{self.author} : {self.thema}'


def file_folder(instance, filename):
    if filename.split('.')[1] is not 'py':
        filename = instance.title + '.' + filename.split('.')[1]
        return "additional/{0}".format(filename)
    else:
        raise Exception


class AdditionalFiles(models.Model):
    file = models.FileField(upload_to=file_folder, verbose_name="Документ")
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, verbose_name="Назва документу")
    pub_date = models.DateField(default=datetime.date.today, blank=True)

    def __str__(self):
        return f'{self.group.number} : {self.title}'
