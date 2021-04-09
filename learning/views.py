from learning.admin import Company_logoAdmin
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from .models import (
    Category,
    Company_logo,
    Contacts,
    Title,
    Courses,
    News,
    Staff,
    About_us,
)


def top_and_bot_logo(request):
    logo = Company_logo.objects.get(pk=1)
    context = {
        "nav_logo": logo,
    }
    return context


def contacts(request):
    contact = Contacts.objects.get(pk=1)
    context = {
        "contact": contact,
    }
    return context


def index(request):
    nav_logo = top_and_bot_logo(request)
    contact = contacts(request)
    title = Title.objects.get(pk=1)
    courses = Courses.objects.all()[:4]
    news = News.objects.all()[:3]
    count = Courses.objects.count()
    context = {
        "title": title,
        "courses": courses,
        "count": count,
        "news": news,
    }
    context.update(nav_logo)
    context.update(contact)
    return render(request, "index.html", context)


def courses(request):
    nav_logo = top_and_bot_logo(request)
    contact = contacts(request)
    queryset = Courses.objects.all()
    title = Title.objects.get(pk=1)
    category = Category.objects.all()
    context = {
        "queryset": queryset,
        "title": title,
        "category": category,
    }
    context.update(nav_logo)
    context.update(contact)
    return render(request, "courses.html", context)


def selected_course(request, slug):
    nav_logo = top_and_bot_logo(request)
    contact = contacts(request)
    title = Title.objects.get(pk=1)
    course = get_object_or_404(Courses, slug=slug)
    document = course.document.all()
    context = {
        "course": course,
        "title": title,
        "document": document,
    }
    context.update(nav_logo)
    context.update(contact)
    return render(request, "selected-course.html", context)


def news(request):
    nav_logo = top_and_bot_logo(request)
    contact = contacts(request)
    title = Title.objects.get(pk=1)
    news = News.objects.all()
    context = {
        "news": news,
        "title": title,
    }
    context.update(nav_logo)
    context.update(contact)
    return render(request, "news.html", context)


def selected_news(request, pk):
    nav_logo = top_and_bot_logo(request)
    contact = contacts(request)
    title = Title.objects.get(pk=1)
    news = get_object_or_404(News, pk=pk)
    context = {
        "news": news,
        "title": title,
    }
    context.update(nav_logo)
    context.update(contact)
    return render(request, "selected-news.html", context)


def about_us(request):
    nav_logo = top_and_bot_logo(request)
    contact = contacts(request)
    title = Title.objects.get(pk=1)
    staff = Staff.objects.all()[:4]
    about = About_us.objects.get(pk=1)
    print(about.documents)
    context = {
        "staff": staff,
        "about": about,
        "title": title,
    }
    return render(request, "about.html", context)
