from django.shortcuts import render

# Create your views here.
# view视图就是python函数，接收请求，处理，做出响应,用户输入的路由就是request
# 路由是我们规定的
from  django.http import HttpRequest
from  django.http import HttpResponse
def index(request):

    return HttpResponse('ok')