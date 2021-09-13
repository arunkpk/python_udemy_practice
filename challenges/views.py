from django.http.response import Http404, HttpResponseNotFound
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("<h1>Home Page This Is !<h1>")


def month(request, month):
    return_text = None
    if month == "jan" or "1" :
        return_text = "<h1>Jan is the month<h1>"
    elif month == "feb":
        return_text = "<h1>feb is the month<h1>"
    elif month == "march":
        return_text = "<h1>march is the month<h1>"
    else:
        return HttpResponseNotFound("<h1>Bad request<h1>")
    return HttpResponse(return_text)
