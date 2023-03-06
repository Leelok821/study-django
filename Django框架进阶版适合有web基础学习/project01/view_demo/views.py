from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.utils.decorators import method_decorator

import time


# Create your views here.
def decora(func):
    def warp(request, *agrs, **kargs):
        start = time.time()
        reslt = func(request, *agrs, **kargs)
        stop = time.time()
        print(f'运行时间:{stop - start}')
        return reslt
    return warp


class VeiwsDemo(View):

    @method_decorator(decora)
    def get(self, request):
        return HttpResponse('这里的Veiw类视图的get方法')
    
    def post(self, request):
        return HttpResponse('这里的Veiw类视图的post方法')


@decora
def add(name):
    name = name + 1
    print(1+2)

add(11)

