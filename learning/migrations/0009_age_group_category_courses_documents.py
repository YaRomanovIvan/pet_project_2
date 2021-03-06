# Generated by Django 3.1.6 on 2021-02-26 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0008_auto_20210226_1209'),
    ]

    operations = [
        migrations.CreateModel(
            name='Age_group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=35, verbose_name='Возрастная группа')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Возрастные группы',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35, verbose_name='Название категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории курсов',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название документа')),
                ('document', models.FileField(upload_to='', verbose_name='Документ')),
            ],
            options={
                'verbose_name': 'Документ',
                'verbose_name_plural': 'Документы',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Не более 80 символов включая пробелы', max_length=80, verbose_name='Название курса')),
                ('description', models.TextField(verbose_name='Описание курса')),
                ('period', models.CharField(help_text='Например "1 января - 1 февраля" или "2 месяца". Желательно придерживаться единого формата.', max_length=35, verbose_name='Период/продолжительность')),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('price', models.PositiveIntegerField(verbose_name='Стоимость курса')),
                ('age_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='age_group', to='learning.age_group', verbose_name='Возрастная группа')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='learning.category', verbose_name='Категория')),
                ('document', models.ManyToManyField(help_text='Выделите нужные документы использую клавишу "ctrl"', to='learning.Documents', verbose_name='Документы')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
                'ordering': ['-pk'],
            },
        ),
    ]
