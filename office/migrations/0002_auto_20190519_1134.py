# Generated by Django 2.0.6 on 2019-05-19 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='files',
            options={'verbose_name': 'Файл', 'verbose_name_plural': 'Файли'},
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'Група', 'verbose_name_plural': 'Групи'},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'verbose_name': 'Предмет', 'verbose_name_plural': 'Предмети'},
        ),
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': 'Викладач', 'verbose_name_plural': 'Викладачі'},
        ),
    ]
