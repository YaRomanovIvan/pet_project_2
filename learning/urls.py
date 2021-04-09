from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("courses/", views.courses, name="courses"),
    path("courses/<slug:slug>", views.selected_course, name="selected_course"),
    path("news/", views.news, name="news"),
    path("news/<int:pk>", views.selected_news, name="selected_news"),
    path("about_us/", views.about_us, name="about_us"),
]
