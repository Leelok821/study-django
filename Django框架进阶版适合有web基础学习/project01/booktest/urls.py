# -*- coding:utf-8 -*-
'''
# Author: li zi hao
'''


from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookListView.as_view()),
    path('books/<int:id>/', views.BookDetail.as_view()),
]