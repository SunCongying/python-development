from django.utils.deprecation import MiddlewareMixin

class TestMiddleWare1(MiddlewareMixin):
    def process_request(self,request):
        print('111111111111111111每次请求前 都会调用执行')
        username = request.COOKIES.get('name')
        if username is None:
            print('没有用户信息')
        else:
            print('有用户信息')
    def process_response(self,request,response):
        print('每次响应前 都会调用执行111111111111111')
        return response
class TestMiddleWare2(MiddlewareMixin):
    def process_request(self,request):
        print('22222222222222每次请求前 都会调用执行')
        username = request.COOKIES.get('name')
        if username is None:
            print('没有用户信息')
        else:
            print('有用户信息')
    def process_response(self,request,response):
        print('每次响应前 都会调用执行2222222222222')
        return response