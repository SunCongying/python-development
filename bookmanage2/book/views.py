from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from book.models import BookInfo
# Create your views here.

# 在书籍表中加入新的信息
def create_book(request):
    book = BookInfo.objects.create(
        name = 'abc',
        pub_date = '2024-1-1',
        readcount = 10,
    )

    return HttpResponse('create')