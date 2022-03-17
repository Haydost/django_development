from urllib import request
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

monthly_ch_dict = {
    "january": "Walk 20min every day",
    "february": "Read book at least 20min before sleep",
    "march": "learn Django 30min every day",
    "april": "Walk 20min every day",
    "may": "Read book at least 20min before sleep",
    "june": "learn Django 30min every day",
    "july": "Walk 20min every day",
    "august": "Read book at least 20min before sleep",
    "september": "learn Django 30min every day",
    "october": "Walk 20min every day",
    "november": "Read book at least 20min before sleep",
    "december": "learn Django 30min every day"

}


def index(request):
    months = list(monthly_ch_dict.keys())
    list_items = ""
    for month in months:
        cap_month=month.capitalize()
        month_list = reverse("month-challenge", args=[month])
        list_items += f"<li><a href='{month_list}'>{cap_month}</a></li>"
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def Monthly_num(request, month):
    monthly_ch_list = list(monthly_ch_dict.keys())
    if month <= len(monthly_ch_list):
        redirect_month = monthly_ch_list[month-1]
        redirect_path = reverse("month-challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    else:
        return HttpResponseNotFound("<h1> number entered for month is greater than 12! </h1>")


def Monthly_str(request, month):
    try:
        challange_text = monthly_ch_dict[month]
        returned_resp = f"<h1> {challange_text} </h1>"
        return HttpResponse(returned_resp)
    except:
        return HttpResponseNotFound("<h1> Not defined </h1>")
