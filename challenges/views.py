from typing import KeysView
from django.http import response
from django.http.response import Http404, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

monthly_challenges = {
    "January": "Jan is the month",
    "February": "February is the month",
    "March": "March is the month",
    "April": "April is the month",
    "May": "May is the month",
    "June": "June is the month",
    "July": "July is the month",
    "August": "August is the month",
    "September": "September is the month",
    "October": "October is the month",
    "November": "November is the month",
    "December": "December is the month"
}

def home(request):
    
    list_months=list(monthly_challenges.keys())
    
    print(type(list_months))

    url_text="http://127.0.0.1:8000/challenges"
    
    return_text=""

    for keys in list_months:
            return_text += f"<li><a href={url_text}/{keys}>{keys}</a></li>"
            print(keys) 
                    
    return HttpResponse("<ul style=\"list-style-none:none\">"+return_text+"</ul>")




def month_number(request, month_key):
    print(month_key)

    #value_list = list(monthly_challenges.values())
    # month_value=value_list[month_key-1]
    # return HttpResponseRedirect(month_value)

    # Redirecting URLS
    if month_key > 0 and month_key < 13:
        key_month_list = list(monthly_challenges.keys())
        month = key_month_list[month_key-1]
        redirect_path = reverse("monthly_challenges_string", args=[month])

    else:
        return HttpResponseNotFound("<h1>Bad Request<h1> <p1> No such month with key <p1>  " + str(month_key))

    return HttpResponseRedirect(redirect_path)


def month(request, month_str):
    return_text = None
    print(month_str)
    try:
        return_text = monthly_challenges[month_str]
        redirect_text = f"<h1>{return_text}</h1>"
    except:
        return_text_1 = "Bad request"
        response_text_1 = f"<h1>{return_text_1}</h1>"
        return HttpResponseNotFound(response_text_1)
    return HttpResponse(redirect_text)
