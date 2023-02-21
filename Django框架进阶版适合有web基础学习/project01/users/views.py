from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.

def index(request):
    return HttpResponse('this is app_users index')

def redirect_demo(request):
    return redirect('/app01/index224')

def reverse_demo(request):
    return redirect(reverse('app01:index'))

def cookie_demo(request):
    res = HttpResponse()
    res.set_cookie('cookie_name','cookie_value',max_age=3500)
    print(request.COOKIES.get('cookie_name'))
    return res

def session_demo(request):
    request.session['tester'] = 'lee'
    return HttpResponse('ok')