from django.db import models
from profiles.models import Profile
import datetime

class Feedback(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    thema = models.CharField(max_length=220)
    message = models.TextField()
    available = models.BooleanField(default=True, blank=True)
    pub_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f'{self.author} : {self.thema}'

