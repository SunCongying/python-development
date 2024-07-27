from django.urls import path
from book.views import create_book,shop


urlpatterns = [
    path('create/',create_book),
    path('11000/11005/',shop),  # 如果有很多类似的路由，比如11004，11003等，定义一个符号'<city_id>/shop_id'
    path('<city_id>/<shop_id>/',shop),  # view中的shop函数要接收这两个参数，获取URL路径中的参数
]