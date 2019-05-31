from django.db import models
from django.db.models.signals import post_delete
from utils import file_cleanup


def image_folder(instance, filename):
    return f"images/{filename}"


class Image(models.Model):
    image = models.FileField(upload_to=image_folder, verbose_name="Картинка", unique=True)
    alt = models.CharField(max_length=50, blank=True, verbose_name="Текстовий опис")

    def __str__(self):
        return f"{self.image.url}"

    class Meta:
        verbose_name_plural = "Фотографії"
        verbose_name = "Фото"


post_delete.connect(file_cleanup, sender=Image)  # Removing file from folder


def preview_image_folder(instance, filename):
    filename = instance.title + '.' + filename.split('.')[1]
    folder = f'news_preview_images/{instance.pk}'
    return f"{folder}/{filename}"


class News(models.Model):
    title = models.TextField(max_length=120, verbose_name="Заголовок новини")
    short_description = models.TextField(verbose_name="Короткий опис новини", blank=True)
    description = models.TextField(verbose_name="Повний опис новини")
    pub_date = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата')

    preview_image = models.ImageField(upload_to=preview_image_folder, verbose_name="Головна картинка", unique=True)
    images = models.ManyToManyField(Image, verbose_name="Додаткові картинки", blank=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name_plural = "Новини"
        verbose_name = "Новина"

post_delete.connect(file_cleanup, sender=News)  # Removing file from folder
