from django.urls import path
from .import views

urlpatterns = [
    path("",views.home,name="home"),    
    path("<int:month_key>",views.month_number,name="monthly_challenges_int"), 
    path("<str:month_str>",views.month,name="monthly_challenges_string")   
]