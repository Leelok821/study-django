# -*- coding:utf-8 -*-
'''
# Author: li zi hao
'''


from django.urls import path
from . import views

urlpatterns = [
    'books/', views.Books.as_view(),
    'book/<id:int>', views.Book.as_view(),
]