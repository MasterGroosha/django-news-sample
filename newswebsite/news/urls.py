from django.urls import path

from . import views

app_name = "news"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:news_date>", views.view_by_date, name="view_by_date")
]
