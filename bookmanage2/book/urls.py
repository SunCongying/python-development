from django.urls import path, register_converter
from book.views import create_book,shop,register,json,method
from book.views import response,set_cookie,get_cookie,set_session,get_session,LoginView,OrderView

# 1.定义转换器
class MobileConverter:
    regex = '1[3-9]\d{9}'

    def to_python(self,value):
        # 将验证没有问题的数据，传递给视图函数
        return value
    # def to_url(self,value):
    #     # 将匹配结果用于反向解析传值时使用，（了解）
    #     return value
# 2.注册转换器
# converter 转换器类
# type_name  转换器名字
register_converter(MobileConverter,'phone')


urlpatterns = [
    path('create/',create_book),
    path('11000/11005/',shop),  # 如果有很多类似的路由，比如11004，11003等，定义一个符号'<city_id>/shop_id'

    # <转换器名字：变量名>
    # 转换器会对变量数据进行 正则的验证

    path('<int:city_id>/<phone:mobile>/',shop),  # view中的shop函数要接收这两个参数，获取URL路径中的参数
    path('register/',register),
    path('json/',json),
    path('method/',method),
    path('res/',response),
    path('set_cookie/',set_cookie),
    path('get_cookie/',get_cookie),
    path('set_session/',set_session),
    path('get_session/',get_session),

    ################类视图###########################################
    path('163login/',LoginView.as_view()), # 这里path的第二个参数是视图函数名，由于LoginView是个类，需要将其转换为视图函数
    path('order/',OrderView.as_view())  # 订单页面，登录才能查看

]