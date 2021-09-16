from typing import KeysView
from django.http.response import Http404, HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("<h1>Home Page This Is !<h1>")


monthly_challenges={
    "January":"<h1>Jan is the month<h1>",
    "February":"<h1> February is the month<h1>",
    "March":"<h1> March is the month<h1>",
    "April":"<h1> April is the month<h1>",
    "May":"<h1> May is the month<h1>",
    "June":"<h1> June is the month<h1>",
    "July":"<h1> July is the month<h1>",
    "August":"<h1> August is the month<h1>",
    "September":"<h1> September is the month<h1>",
    "October":"<h1> October is the month<h1>",
    "November":"<h1> November is the month<h1>",
    "December":"<h1> December is the month<h1>",
}

def month_number(request,month_key):
    return_text = None    
    print(month_key)    
    values_1=monthly_challenges.values()    
    value_list = list(values_1)
    month_value=value_list[month_key-1]
    return HttpResponse(month_value)

def month(request, month):
    return_text = None
    print(month)
    try:
        return_text=monthly_challenges[month]
    except:
        return HttpResponseNotFound("<h1>Bad request<h1>")
    return   HttpResponse(return_text)
