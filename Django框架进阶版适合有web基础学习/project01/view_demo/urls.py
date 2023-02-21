from django.urls import path
from view_demo.views import *

urlpatterns = [
    path('views_demo/', VeiwsDemo.as_view())
    # path('views_demo/', decora(VeiwsDemo.as_view()))
]