from datetime import date, timedelta

from django.http import HttpResponse
from django.template import loader


# Create your views here.


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
