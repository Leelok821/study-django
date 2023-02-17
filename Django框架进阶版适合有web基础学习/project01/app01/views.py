from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.


def index(request):
    return HttpResponse('hello world')

def index2(request):
    return HttpResponse('hello world2')

def weather(request, city):
    return HttpResponse(f'{city} weather is lalalan')

def get_qurey_params(request):
    query_dict = request.GET
    name = query_dict.get('name')
    age = query_dict.get('age')
    l = query_dict.getlist('name')

    print(name, age, l)
    return HttpResponse(f'get_query')

def get_form_data(request):
    qd = request.POST
    name = qd.get('name')
    age = qd.get('age')
    l = qd.getlist('name')
    print(name, age, l)
    return HttpResponse(f'get_form_data')

def get_json_data(request):
    data_byte = request.body    #返回二进制数据
    json1 = data_byte.decode()
    import json
    result = json.loads(json1)
    print(result)
    print(request.META)
    print(request.user)
    return HttpResponse(f'get_json_data')


def get_response(request):
    data = {"11":22,"22":'ss'}
    return JsonResponse(data,status=500)

def test(request):
    data = {}