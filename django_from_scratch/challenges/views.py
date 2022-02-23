from urllib import request
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

monthly_ch_dict = {
    "January": "Walk 20min every day",
    "February": "Read book at least 20min before sleep",
    "March": "learn Django 30min every day",
    "April": "Walk 20min every day",
    "May": "Read book at least 20min before sleep",
    "June": "learn Django 30min every day",
    "July": "Walk 20min every day",
    "August": "Read book at least 20min before sleep",
    "September": "learn Django 30min every day",
    "October": "Walk 20min every day",
    "November": "Read book at least 20min before sleep",
    "December": "learn Django 30min every day"

}


def Monthly_num(request, month):
    monthly_ch_list = list(monthly_ch_dict.keys())
    if month <= 12:
        redirect_month = monthly_ch_list[month-1]
        redirect_path = reverse("month-challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    else:
        return HttpResponseNotFound("number entered for month is greater than 12")


def Monthly_str(request, month):
    try:
        return HttpResponse(monthly_ch_dict[month])
    except:
        return HttpResponseNotFound("Not defined")
