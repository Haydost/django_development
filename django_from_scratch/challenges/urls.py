
from django.urls import path
from . import views

urlpatterns = [
    path("<int:month>", views.Monthly_num),
    path("<str:month>", views.Monthly_str)
]
