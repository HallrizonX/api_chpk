from django.db import models

from profiles.models import Profile
from office.models import Subject


class Student(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, verbose_name="Профіль студента")
    subjects = models.ManyToManyField(Subject, blank=True, verbose_name="Предмети студента ")

    def __str__(self) -> str:
        return "{} {} {}".format(self.profile.name, self.profile.surname, self.profile.last_name)

    class Meta:
        verbose_name: str = "Студент"
        verbose_name_plural: str = "Студенти"


class Mark(models.Model):
    mark = models.CharField(max_length=2, verbose_name='Оцінка')
    date = models.DateField(verbose_name='Дата')

    def __str__(self):
        return f'Оцінка-{self.mark} | День-{self.date.day} Місяць-{self.date.month} Рік-{self.date.year}'

    class Meta:
        verbose_name: str = "Відмітка"
        verbose_name_plural: str = "Відмітки"


class Rating(models.Model):
    subject = models.ForeignKey(Subject, blank=True, on_delete=models.CASCADE, verbose_name="Предмет")
    marks = models.ManyToManyField(Mark, blank=True, verbose_name="Оцінки")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Студент")

    def __str__(self):
        return f'{self.student.profile.surname} {self.student.profile.name} {self.student.profile.last_name}, {self.subject.name}'

    class Meta:
        verbose_name: str = "Журнал"
        verbose_name_plural: str = "Журнали"