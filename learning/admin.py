from django.contrib import admin
from django.db import models

from .models import (
    Company_logo,
    Contacts,
    Title,
    Category,
    Age_group,
    Documents,
    Courses,
    News,
    About_us,
    Staff,
)


class Company_logoAdmin(admin.ModelAdmin):
    list_display = ("top_logo", "top_logo_mobile")


class ContactsAdmin(admin.ModelAdmin):
    list_display = ("address", "telephone", "email")


class TitleAdmin(admin.ModelAdmin):
    list_display = ("title", "slogan", "description")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


class Age_groupAdmin(admin.ModelAdmin):
    list_display = ("group",)


class DocumentsAdmin(admin.ModelAdmin):
    list_display = ("name", "document")


class CoursesAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "age_group", "period")
    prepopulated_fields = {"slug": ("name",)}


class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "date")


class StaffAdimn(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "position")


class AboutusAdmin(admin.ModelAdmin):
    list_display = ("pk", "text")


admin.site.register(Company_logo, Company_logoAdmin)
admin.site.register(Contacts, ContactsAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Age_group, Age_groupAdmin)
admin.site.register(Documents, DocumentsAdmin)
admin.site.register(Courses, CoursesAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(About_us, AboutusAdmin)
admin.site.register(Staff, StaffAdimn)
