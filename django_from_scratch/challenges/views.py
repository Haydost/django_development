from django.http import HttpResponseNotFound, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse
#from django.template.loader import render_to_string
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
    "december": None

}


def index(request):
    months = list(monthly_ch_dict.keys())
    return render(request, "challenges/index.html", {
        "month_k": months
    })
    #list_items = ""
    # for month in months:
    #    cap_month = month.capitalize()
    #    month_list = reverse("month-challenge", args=[month])
    #    list_items += f"<li><a href='{month_list}'>{cap_month}</a></li>"
    #response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)


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
        #returned_resp = f"<h1> {challange_text} </h1>"
        #returned_resp = render_to_string("challenges/challenge.html")
        # return HttpResponse(returned_resp)
        return render(request, "challenges/challenge.html", {
            "text": challange_text,
            "month_name": month
        })
    except:
        #response_data = render_to_string("404.html")
        #return HttpResponseNotFound(response_data)
        raise Http404("Not Found")