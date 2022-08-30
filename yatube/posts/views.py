from django.shortcuts import render

from django.http import HttpResponse


# Главная страница
def index(request):
    template = 'posts/index.html'
    title = 'Это главная страница проекта Yatube'
    context = {
        'title': title,
    }
    return render(request, template, context)


# Страница для постов;
def group_posts(request, slug):
    return HttpResponse(f'Страница для общих постов {slug}')


def group_list(request):
    template = 'posts/group_list.html'
    title = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'title': title,
    }
    return render(request, template, context)
