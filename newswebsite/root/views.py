from django.http import HttpResponse


def index(request):
    return HttpResponse(f"Пожалуйста, откройте страницу по ссылке <a href='/news/'>НОВОСТНОЙ САЙТ</a>")
