from django.shortcuts import render
from django.http import HttpResponse


# def index(request):
#     # print(dir(request))
#     return HttpResponse('Hello world')


def lab(request):
    return HttpResponse('<h1>Тестовая страница</h1>')





def index(request):
    # news = News.objects.all()
    # context = {
    #     'news': news,
    #     'title': 'Список новостей'
    # }
    # return render(request, template_name='news/index.html', context=context)
    return render(request, template_name='covidlab/index.html')
