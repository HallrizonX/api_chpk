from django.db import models
from django.contrib.auth.models import User

ACCESS_PROFILES = (
    ('teacher', 'Teacher'),
    ('student', 'Student'),
    (None, None),
)


class Profile(models.Model):
    user = models.ForeignKey(User, verbose_name="Юзер", on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name="Ім'я", blank=True)
    surname = models.CharField(max_length=50, verbose_name="Прізвище", blank=True)
    last_name = models.CharField(max_length=50, verbose_name="По батькові", blank=True)

    access = models.CharField(max_length=10, blank=True, verbose_name="Офіс користувача", choices=ACCESS_PROFILES,
                              default=None)

    def __str__(self):
        return f"{self.surname} {self.name} {self.last_name}"



    class Meta:
        verbose_name = "Профіль"
        verbose_name_plural = "Профілі"

