from django.db import models
from profiles.models import Profile
from django.urls import reverse
from django.db.models.signals import post_delete, pre_save

from utils import file_cleanup, change_profile_from_teacher


class Group(models.Model):
    number = models.CharField(max_length=4, unique=True, verbose_name="Номер групи")

    def __str__(self) -> str:
        return f"Група: {self.number}"

    @property
    def get_teachers(self):
        return Teacher.objects.filter(groups__number=self.number)

    class Meta:
        verbose_name: str = "Група"
        verbose_name_plural: str = "Групи"


class Subject(models.Model):
    """ Table for saving subject"""
    name = models.CharField(max_length=120, verbose_name="Назва предмету")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Група в якій буде викладатися")

    def __str__(self) -> str:
        return f"Предмет - {self.name}, група - {self.group.number}"

    def get_teachers(self):
        return Teacher.objects.filter(subjects__in=self.id)

    class Meta:
        verbose_name: str = "Предмет"
        verbose_name_plural: str = "Предмети"


def file_folder(instance, filename):
    if filename.split('.')[1] is not 'py':
        filename = instance.title + '.' + filename.split('.')[1]
        return "files/{0}".format(filename)
    else:
        raise Exception


class Files(models.Model):
    """ Table for saving files"""
    file = models.FileField(upload_to=file_folder, verbose_name="Документ")
    title = models.CharField(max_length=120, verbose_name="Назва документу")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,
                                verbose_name="Предмет до якого буде відноситися документ")

    def __str__(self) -> str:
        return f"{self.title} - {self.subject.name}"

    def get_absolute_url(self) -> str:
        return reverse("media", kwargs={"slug": self.file.path})

    @property
    def get_subject(self) -> Subject:
        return Files.objects.get(subject=self.subject)

    class Meta:
        verbose_name: str = "Файл"
        verbose_name_plural: str = "Файли"


post_delete.connect(file_cleanup, sender=Files)  # Removing file from folder


class Teacher(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, verbose_name="Профіль викладача")
    subjects = models.ManyToManyField(Subject, blank=True, verbose_name="Предмети викладача")
    files = models.ManyToManyField(Files, blank=True, verbose_name="Файли викладача", related_name='teachers')
    groups = models.ManyToManyField(Group, blank=True, verbose_name="Групи в яких викладає викладач",
                                    related_name='teachers')

    def __str__(self) -> str:
        return "{} | {} {} {}".format(self.profile.user.username, self.profile.name, self.profile.surname,
                                      self.profile.last_name)

    @property
    def get_subjects(self) -> Subject:
        return Subject.objects.filter(teacher__profile=self.profile)

    @property
    def get_groups(self) -> Group:
        return Group.objects.filter(teachers__profile=self.profile)

    @property
    def get_files(self) -> Files:
        return Files.objects.filter(teachers__profile=self.profile)

    class Meta:
        verbose_name: str = "Викладач"
        verbose_name_plural: str = "Викладачі"


pre_save.connect(change_profile_from_teacher, sender=Teacher)  # Adding to field access value 'teacher'
