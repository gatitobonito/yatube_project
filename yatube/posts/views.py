from django.shortcuts import render

from django.http import HttpResponse


# Главная страница
def index(request):
    template = 'posts/index.html'
    return render(request, template)


# Страница для постов;
def group_posts(request, slug):
    return HttpResponse(f'Страница для общих постов {slug}')

def group_list(request):
    template = 'posts/group_list.html'
    return render(request, template)
