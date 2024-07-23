from django.shortcuts import render

# Create your views here.
# view视图就是python函数，接收请求，处理，做出响应,用户输入的路由就是request
# 路由是我们规定的
from  django.http import HttpRequest
from  django.http import HttpResponse
def index(request):

    # return HttpResponse('ok')

    # 假设context是数据库中的内容
    context={
        'name':"马上双十一，点击有惊喜"
    }
    return render(request,template_name='book/index.html',context=context)   # render就是渲染模板