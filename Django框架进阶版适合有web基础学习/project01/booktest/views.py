from django.shortcuts import render

# Create your views here.


from models import BookInfo

"""新增"""

book = BookInfo()
book.btitle = '三国'
book.bpub_date = '1942-2-1'
book.save()

BookInfo.objects.create(
    btitle = '西游记',
    bpub_date = '1933-2-22'
)

BookInfo.objects.filter(btitle__contains='西游')