from django.urls import path
from app01 import views

urlpatterns = [
    path('index/', views.index),
    path('index224/', views.index2),
    path('weather/<str:city>', views.weather),
    path('get_qurey_params/', views.get_qurey_params),
    path('get_form_data/', views.get_form_data),
    path('get_json_data/', views.get_json_data),
    path('get_response/', views.get_response),
]
