# Generated by Django 2.0.6 on 2019-05-20 09:41

from django.db import migrations, models
import news.models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='short_description',
            field=models.TextField(blank=True, max_length=300, verbose_name='Короткий опис новини'),
        ),
        migrations.AlterField(
            model_name='image',
            name='alt',
            field=models.CharField(blank=True, max_length=50, verbose_name='Текстовий опис'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.FileField(unique=True, upload_to=news.models.image_folder, verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.TextField(verbose_name='Повний опис новини'),
        ),
        migrations.AlterField(
            model_name='news',
            name='preview_image',
            field=models.ImageField(unique=True, upload_to=news.models.preview_image_folder, verbose_name='Головна картинка'),
        ),
    ]
