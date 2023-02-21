# -*- coding:utf-8 -*-
'''
# Author: li zi hao
'''

from django.urls import path
from users.views import *

urlpatterns = [
    path('index/', index, name='index'),
    path('redirect_demo/', redirect_demo),
    path('reverse_demo/', reverse_demo),
    path('cookie_demo/', cookie_demo),
    path('session_demo/', session_demo),
]