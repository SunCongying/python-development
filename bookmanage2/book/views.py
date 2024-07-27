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


def shop(request,city_id,shop_id):

    print(city_id,shop_id)

    return HttpResponse('贝贝的小饭店')

"""
查询字符串

url以？为分割
？   前面的是路径  
    后面的是查询字符串，为字典形式，多个数据采用&拼接


"""