from django.urls import path
from .import views

urlpatterns = [
    path("",views.home,name="home"),
    path("<int:month_key>",views.month_number,name="int_month"), 
    path("<str:month>",views.month,name="str_month")   
]