# Generated by Django 3.1.6 on 2021-04-09 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0015_auto_20210226_1441'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('position', models.CharField(max_length=40, verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
                'ordering': ['position'],
            },
        ),
        migrations.CreateModel(
            name='About_us',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Описание')),
                ('image_1', models.ImageField(upload_to='', verbose_name='Изображение 1')),
                ('image_2', models.ImageField(upload_to='', verbose_name='Изображение 2')),
                ('documents', models.ManyToManyField(help_text='Выделите нужные документы использую клавишу "ctrl"', related_name='doc_about', to='learning.Documents', verbose_name='Документы')),
            ],
            options={
                'verbose_name': 'О нас',
                'verbose_name_plural': 'О нас',
                'ordering': ['pk'],
            },
        ),
    ]