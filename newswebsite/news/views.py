from datetime import date, timedelta
from random import sample

from django.http import HttpResponse
from django.template import loader

headlines = [
    "iPhone 14 Pro подешевел в России",
    "Раскрыты подробные характеристики пикапа Tesla Cybertruck",
    "Поставки компьютеров вырастут из-за искусственного интеллекта",
    "Под поверхностью Марса обнаружили многоугольные объекты",
    "В ChatGPT обнаружили уязвимость",
    "Метеозависимым людям подсказали способы легче перенести магнитную бурю",
    "Обнаружен самый слабый спутник Млечного Пути",
    "Детеныш панды из Московского зоопарка начал ползать и попал на видео",
    "Бактерии в йогурте предотвратили развитие психических расстройств",
    "Телескоп Уэбба запечатлел беспрецедентные детали объекта Хербига-Аро",
    "На Алтае медведицу засняли во время кормления малышей",
    "Названы лучшие производители техники из Азии",
    "Создатели «Ведьмака» рассказали о новой части игры",
]


def available_dates():
    dates = list()
    starting_date = date(year=2023, month=11, day=1)
    while starting_date.month != 12:
        dates.append(starting_date)
        starting_date += timedelta(days=1)
    return dates


def index(request):
    template = loader.get_template("news/index.html")
    context = {
        "available_dates": available_dates()
    }
    return HttpResponse(template.render(context, request))


def view_by_date(request, news_date: date):
    template = loader.get_template("news/news_by_date.html")
    context = {
        "news_date": news_date.strftime("%d.%m.%Y"),
        "headlines": sample(headlines, 3)
    }
    return HttpResponse(template.render(context, request))
