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

    ###### 传递参数的四种方式 ###########
    # print(city_id,shop_id)   # 1.获取URL路径中的参数
    query_params=request.GET  # 2.查询字符串  <QueryDict: {'order': ['readcount']}>
    print(query_params)
    order1 = query_params.get('order')  # 获取字典的值，如果字典有多个值，只会获取最后一个
    order2 = query_params.getlist('order')  # 如果字典有多个值，会获取所有值，以列表的形式返回

    # order = query_params['order']  # 获取字典的值
    print(order1)
    print(order2)


    return HttpResponse('贝贝的小饭店')

"""
查询字符串

url以？为分割
？   前面的是路径  
    后面的是查询字符串，为字典形式，多个数据采用&拼接


"""