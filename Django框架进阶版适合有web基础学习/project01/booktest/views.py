from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
from django.views import View


from .models import BookInfo, HeroInfo

import json

# """新增"""

# book = BookInfo()
# book.btitle = '三国'
# book.bpub_date = '1942-2-1'
# book.save()

# BookInfo.objects.create(
#     btitle = '西游记',
#     bpub_date = '1933-2-22'
# )

# BookInfo.objects.filter(btitle__contains='西游')

class BookListView(View):

    def get(self, request):
        # 查询所有数据
        books = BookInfo.objects.all()
        books_l = []
        for book in books:
            book_dic = {
                'btitle':book.btitle,
                'bpub_date':book.bpub_date,
                'bread':book.bread,
                'bcomment':book.bcomment,
            }
            books_l.append(book_dic)
        return JsonResponse(books_l, safe=False, json_dumps_params={"ensure_ascii":False})

    def post(self, request):
        """新增数据"""
        data_byte = request.body
        data_json = data_byte.decode()
        data = json.loads(data_json)

        BookInfo.objects.create(
            btitle=data['btitle'],
            bpub_date=data['bpub_date'],
            bread=data['bread'],
            bcomment=data['bcomment'],
        )
        return JsonResponse(data, status=201)

    
class BookDetail(View):

    def get(self, request, id):
        """书本详情"""

        qs = BookInfo.objects.filter(id=id)
        for book in qs:
            book_dic = {
                'btitle':book.btitle,
                'bpub_date':book.bpub_date,
                'bread':book.bread,
                'bcomment':book.bcomment,
            }
        return JsonResponse(book_dic)
        

    def put(self, request, id):
        data_bytes = request.body
        data_s = data_bytes.decode()
        data = json.loads(data_s)

        try:
            book = BookInfo.objects.get(id=id)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)
        
        book.btitle = data['btitle']
        book.bpub_date = data['bpub_date']
        book.bcomment = data['bcomment']
        book.bread = data['bread']

        book.save()
        return HttpResponse(status=200)

    def delete(self, request, id):
        BookInfo.objects.get(id=id).delete()
        return HttpResponse(status=200)

