from django.db import models
from profiles.models import Profile
from django.urls import reverse
from django.db.models.signals import post_delete, pre_save
from utils import file_cleanup, change_profile_from_teacher


class Group(models.Model):
    """ Table for saving group"""
    number = models.CharField(max_length=4, unique=True, verbose_name="Номер групи")
    slug = models.SlugField(max_length=120, unique=True, verbose_name="URL адреса")

    def __str__(self) -> str:
        return f"Група: {self.number}"

    def get_absolute_url(self) -> str:
        return f"/{self.slug}/"

    class Meta:
        verbose_name: str = "Група"
        verbose_name_plural: str = "Групи"


class Subject(models.Model):
    """ Table for saving subject"""
    name = models.CharField(max_length=120, verbose_name="Назва предмету")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, verbose_name="Група в якій буде викладатися")
    slug = models.SlugField(max_length=120, verbose_name="URL адреса")

    def __str__(self) -> str:
        return f"Предмет - {self.name}, група - {self.group.number}"

    def get_absolute_url(self) -> str:
        return reverse("subject", kwargs={'slug': self.slug})

    class Meta:
        verbose_name: str = "Предмет"
        verbose_name_plural: str = "Предмети"


def file_folder(instance, filename):
    filename = instance.title + '.' + filename.split('.')[1]
    return "files/{0}".format(filename)


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

    class Meta:
        verbose_name: str = "Файл"
        verbose_name_plural: str = "Файли"


post_delete.connect(file_cleanup, sender=Files)  # Removing file from folder


class Teacher(models.Model):
    """ Table for saving teacher in relation profile """
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, verbose_name="Профіль викладача")
    subjects = models.ManyToManyField(Subject, blank=True, verbose_name="Предмети викладача")
    files = models.ManyToManyField(Files, blank=True, verbose_name="Файли викладача")

    def __str__(self) -> str:
        return "{} {} {}".format(self.profile.name, self.profile.surname, self.profile.last_name)

    def get_absolute_url(self) -> str:
        return reverse('teacher', kwargs={"slug": self.profile.user.username})

    class Meta:
        verbose_name: str = "Викладач"
        verbose_name_plural: str = "Викладачі"


pre_save.connect(change_profile_from_teacher, sender=Teacher)  # Adding to field access value 'teacher'
