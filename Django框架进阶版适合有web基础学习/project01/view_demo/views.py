from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.utils.decorators import method_decorator

# Create your views here.
def decora(func):
    def warp(request, *agrs, **kargs):
        print('执行装饰器')
        return func(request, *agrs, **kargs)
    return warp


class VeiwsDemo(View):

    @method_decorator(decora)
    def get(self, request):
        return HttpResponse('这里的Veiw类视图的get方法')
    
    def post(self, request):
        return HttpResponse('这里的Veiw类视图的post方法')




