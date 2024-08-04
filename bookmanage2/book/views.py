from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
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


def shop(request,city_id,mobile):

    ###### 传递参数的四种方式 ###########
    print(city_id,mobile)   # 1.获取URL路径中的参数
    # query_params=request.GET  # 2.查询字符串  <QueryDict: {'order': ['readcount']}>
    # print(query_params)
    # order1 = query_params.get('order')  # 获取字典的值，如果字典有多个值，只会获取最后一个
    # order2 = query_params.getlist('order')  # 如果字典有多个值，会获取所有值，以列表的形式返回
    #
    # # order = query_params['order']  # 获取字典的值
    # print(order1)
    # print(order2)

    return HttpResponse('贝贝的小饭店')

"""
查询字符串

url以？为分割
？   前面的是路径  
    后面的是查询字符串，为字典形式，多个数据采用&拼接

"""

def register(request):
    data = request.POST
    print(data)

    return HttpResponse('表单 ok')

def json(request):
    body = request.body  # json数据不能通过POST获取，要通过body获取
    print(body)
    body_str = body.decode()# 转换为string类型
    print(body_str)
    print(type(body_str))

    import json
    # 将JSON形式的字符串转变为python的字典
    body_dict = json.loads(body_str)

    print(body_dict)

    ##############请求头###################
    print(request.META)  # 字典类型
    print(request.META['SERVER_PORT'])

    return HttpResponse('json ok')

def method(request):

    print(request.method)

    return HttpResponse('method ok')

def response(request):
    # # 响应头
    # response = HttpResponse('res',status=200)
    # response['name']='scyscy'
    # return response
    # return HttpResponse('response ok')

    # JsonResponse
    # info = {
    #     'name' : 'scy',
    #     'address' : 'shannxi'
    # }
    friend = [
        {
            'name': 'zzz',
            'address': 'shannxi'
        },
        {
            'name': 'www',
            'address': 'wuhan'
        }
    ]

    # response = JsonResponse(data =friend,safe=False)
    # return response

    # data返回的响应数据 一般是字典类型,
    # safe = True 表示我们的data是字典数据，
    # JsonResponse 可以将字典转换为json字符串格式
    # 当给的是非字典数据时，要将 safe = False，


    # JsonResponse本质就是使用了json.dumps()函数将字典转换为字符串，
    import json
    data = json.dumps(friend)
    response = HttpResponse(data)
    return response


# HttpResponse(1,2,3)  # 涉及三个参数
# 1.content=响应体，表示返回的内容
# 2.content_type=响应体数据类型
# 3.status=状态码   很重要！
#   1XX
#   2XX
#   3XX
#   4XX
#       403 ：禁止访问，权限问题
#       404 ：找不到页面，路由有问题
#   5XX

################################ Cookie ################################
"""
第一次请求，携带查询字符串
服务器接收到请求之后，获取username，服务器设置cookie信息，cookie信息包括username
http://127.0.0.1:8000/set_cookie/?username=scy&password=20001126
浏览器接收到服务器的响应之后，会把cookie保存起来

第二次及其之后请求，访问http://127.0.0.1:8000/时都会携带cookie信息，

"""
def set_cookie(request):
    # 获取请求中的查询字符串数据
    username = request.GET['username']
    password = request.GET['password']
    # 服务器设置cookie信息
    # 通过响应对象.set_cookie方法
    response = HttpResponse('set_cookie ok')
    response.set_cookie('name',username,max_age=60*60)  # 这里给出的是键，值参数
    response.set_cookie('pwd',password)

    # response.delete_cookie('name')
    # max_age 是一个秒数
    return response

def get_cookie(request):
    # 获取cookies
    # request.COOKIES 获取到字典数据
    print(request.COOKIES)
    name = request.COOKIES.get('name')
    return HttpResponse(name)


################################ Session ################################
# session依赖于cookie，比cookie安全性高一点
"""
第一次请求http://127.0.0.1:8000/set_cookie/?username=scy&password=20001126，
服务器中会设置session信息同时生成一个sessionid的cookie信息
浏览器接收这个cookie信息并将其进行保存

第二次及之后的请求都会携带sessionid，服务器会验证sessionid，验证没问题会读取相关数据，实现业务逻辑
"""
# 数据库是服务器端
def set_session(request):
    # 模拟 获取用户信息
    username = request.GET.get('username')
    # 设置session信息
    user_id = 1
    request.session['user_id'] = user_id
    request.session['username'] = username
    # 设置session的有效期
    request.session.set_expiry(3600)   # 单位为秒
    # 删除session的数据
    # request.session.clear()  # 删除所有session键对应的值
    # request.session.flush()  # 删除所有session键及其对应的值

    return HttpResponse('set_session')

def get_session(request):
    user_id = request.session.get('user_id')
    username = request.session.get('username')

    content = '{},{}'.format(user_id,username)

    return HttpResponse(content)

########################### 类视图 ################################
# 类视图的定义
# 特点：1.继承自view，  2.类视图中的方法是采用 http方法的小写 来区分不同的请求方式
from django.views import View
class LoginView(View):

    def get(self,request):

        return HttpResponse('get get get')

    def post(self,request):

        return HttpResponse('post post post')

########################################################################
"""
我的订单、个人中心页面
如果登录用户 可以访问
如果未登录 不能访问 跳转到登录页面

定义一个订单、个人中心 类视图
"""
"""
多继承（继承多个父类）
python，c++

"""
from django.contrib.auth.mixins import LoginRequiredMixin
# LoginRequiredMixin 的作用是 判断 只有登录用户才可以访问界面

class OrderView(LoginRequiredMixin,View):
    def get(self,request):

        return HttpResponse('GET 我的订单页面，这个页面必须登录才能看见')
