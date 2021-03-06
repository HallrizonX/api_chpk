# Generated by Django 2.0.6 on 2019-05-30 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('office', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.CharField(max_length=2, verbose_name='Оцінка')),
                ('date', models.DateField(verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Відмітка',
                'verbose_name_plural': 'Відмітки',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.ManyToManyField(blank=True, to='journal.Mark', verbose_name='Оцінки')),
            ],
            options={
                'verbose_name': 'Журнал',
                'verbose_name_plural': 'Журнали',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='profiles.Profile', verbose_name='Профіль студента')),
                ('subjects', models.ManyToManyField(blank=True, to='office.Subject', verbose_name='Предмети студента ')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенти',
            },
        ),
        migrations.AddField(
            model_name='rating',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journal.Student', verbose_name='Студент'),
        ),
        migrations.AddField(
            model_name='rating',
            name='subject',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='office.Subject', verbose_name='Предмет'),
        ),
    ]
