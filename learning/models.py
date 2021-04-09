from os import name
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField


class partner_logos(models.Model):
    name = models.CharField(max_length=100, verbose_name="Партнер")
    partner_logos = models.ImageField(verbose_name="Логотипы партнеров")

    class Meta:
        ordering = ["-pk"]
        verbose_name_plural = "Логотипы партнеров"
        verbose_name = "Логотип парнера"

    def __str__(self):
        return self.name


class Contacts(models.Model):
    address = models.CharField(max_length=80, verbose_name="Адрес")
    telephone = models.CharField(
        max_length=15,
        verbose_name="Телефон(факс)",
    )
    email = models.EmailField(verbose_name="Почта")

    class Meta:
        ordering = ["pk"]
        verbose_name_plural = "Контактные данные компании"
        verbose_name = "Адрес, телефон и почта"


class Company_logo(models.Model):
    top_logo = models.ImageField(verbose_name="Логотип в шапке сайта")
    top_logo_mobile = models.ImageField(
        verbose_name="Логотип в шапке сайта (мобильный)"
    )
    bot_logo = models.ImageField(verbose_name="Логотип в подвале сайта")

    class Meta:
        ordering = ["pk"]
        verbose_name_plural = "Логотипы компании"
        verbose_name = "Логотип компании"


class Title(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Заголовок",
        help_text="Не более 200 символов включая пробелы.",
    )
    slogan = models.CharField(
        max_length=60,
        verbose_name="Слоган",
        help_text="Не более 60 символов включая пробелы.",
    )
    description = models.TextField(max_length=180, verbose_name="Описание")
    image = models.ImageField(verbose_name="Изображение рядом с особенностью")
    features = models.TextField(verbose_name="Особенность")

    class Meta:
        ordering = ["pk"]
        verbose_name_plural = "Баннер"
        verbose_name = "Баннер"

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=35, verbose_name="Название категории")

    class Meta:
        ordering = ["pk"]
        verbose_name_plural = "Категории курсов"
        verbose_name = "Категория"

    def __str__(self):
        return self.name


class Age_group(models.Model):
    group = models.CharField(max_length=35, verbose_name="Возрастная группа")

    class Meta:
        ordering = ["pk"]
        verbose_name_plural = "Возрастные группы"
        verbose_name = "Группа"

    def __str__(self):
        return self.group


class Documents(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название документа")
    document = models.FileField(verbose_name="Документ")

    class Meta:
        ordering = ["pk"]
        verbose_name_plural = "Документы"
        verbose_name = "Документ"

    def __str__(self):
        return self.name


class Courses(models.Model):
    name = models.CharField(
        max_length=80,
        help_text="Не более 80 символов включая пробелы",
        verbose_name="Название курса",
    )
    slug = models.SlugField(
        unique=True,
        verbose_name="Слаг",
        help_text="Слаг должен быть уникальным. ",
    )
    description = models.TextField(verbose_name="Описание курса")
    document = models.ManyToManyField(
        Documents,
        verbose_name="Документы",
        help_text='Выделите нужные документы использую клавишу "ctrl"',
        related_name="doc",
    )
    category = models.ForeignKey(
        Category,
        on_delete=CASCADE,
        verbose_name="Категория",
        related_name="category",
    )
    age_group = models.ForeignKey(
        Age_group,
        on_delete=CASCADE,
        verbose_name="Возрастная группа",
        related_name="age_group",
    )
    period = models.CharField(
        max_length=35,
        verbose_name="Период/продолжительность",
        help_text='Например "1 января - 1 февраля" или "2 месяца". Желательно придерживаться единого формата.',
    )
    image = models.ImageField(verbose_name="Изображение")
    price = models.PositiveIntegerField(verbose_name="Стоимость курса")

    class Meta:
        ordering = ["-pk"]
        verbose_name_plural = "Курсы"
        verbose_name = "Курс"

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(
        max_length=150,
        verbose_name="Заголовок",
        help_text="Не более 150 символов включая пробелы",
    )
    date = models.DateField(auto_now_add=True, verbose_name="Дата")
    description = models.TextField(verbose_name="Описание")
    title_image = models.ImageField(verbose_name="Главное изображение")
    image = models.ImageField(
        verbose_name="Изображение",
        help_text="Не обязательно для заполнения.",
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ["-pk"]
        verbose_name_plural = "Новости"
        verbose_name = "Новость"

    def __str__(self):
        return self.title


class Staff(models.Model):
    first_name = models.CharField(max_length=30, verbose_name="Имя")
    last_name = models.CharField(max_length=30, verbose_name="Фамилия")
    position = models.CharField(max_length=40, verbose_name="Должность")
    image = models.ImageField(
        verbose_name="Фото",
        blank=True,
    )

    class Meta:
        ordering = ["position"]
        verbose_name_plural = "Сотрудники"
        verbose_name = "Сотрудник"

    def __str__(self):
        return f"{self.last_name}, {self.position}"


class About_us(models.Model):
    text = models.TextField(verbose_name="Описание")
    image_1 = models.ImageField(verbose_name="Изображение 1")
    image_2 = models.ImageField(verbose_name="Изображение 2")
    documents = models.ManyToManyField(
        Documents,
        verbose_name="Документы",
        help_text='Выделите нужные документы использую клавишу "ctrl"',
        related_name="doc_about",
    )

    class Meta:
        ordering = ["pk"]
        verbose_name_plural = "О нас"
        verbose_name = "О нас"
