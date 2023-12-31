from datetime import date, datetime

from django.urls import path, register_converter

from . import views


class DateConverter:
    regex = r"\d{4}\-(0[1-9]|1[012])\-(0[1-9]|[12][0-9]|3[01])"
    format = "%Y-%m-%d"

    def to_python(self, value: str) -> date:
        return datetime.strptime(value, self.format).date()

    def to_url(self, value: str) -> str:
        return value


register_converter(DateConverter, "published_date")


class CityConverter:
    regex = r"[a-z]*"

    def to_python(self, value: str) -> str:
        if value not in {"moscow", "omsk", "vladivostok"}:
            raise ValueError
        return value

    def to_url(self, value: str) -> str:
        return value


register_converter(CityConverter, "city_converter")


app_name = "news"
urlpatterns = [
    path("", views.index, name="index"),
    path("<published_date:news_date>/", views.view_by_date, name="view_by_date"),
    path("<city_converter:city>/", views.view_by_city, name="view_by_city"),
]
