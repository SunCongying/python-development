from django.shortcuts import render

# Create your views here.
# view视图就是python函数，接收请求，处理，做出响应,用户输入的路由就是request
# 路由是我们规定的
from  django.http import HttpRequest
from  django.http import HttpResponse
def index(request):
    # 在这里实现增删改查，但是这种方式需要每次都运行工程，然后使用浏览器发出请求才能查看结果，比较麻烦
    # 使用shell输入每条指令后就会给出对应的结果，python manage.py shell
    #-----------------------------
    return HttpResponse('ok')


    # 假设context是数据库中的内容
    #-------------------------------
    # context={
    #     'name':"马上双十一，点击有惊喜"
    # }
    # return render(request,template_name='book/index.html',context=context)   # render就是渲染模板
    # ---------------------------
############## 增加数据  ########################
from book.models import BookInfo
# 方式1,必须调用对象的save方法才能将数据保存到数据库中
book = BookInfo(
    name='Django',
    pub_date='2000-1-1',
    readcount=10
)
book.save()

# 方式2，不需要调用save，会自动保存到数据库中
# objects ---- 相当于一个代理，实现增删改查
BookInfo.objects.create(
    name='会不会出现字',
    pub_date='2024-1-1',
    readcount=24
)

################ 修改数据 #########################
# 方式一,使用save保存
book = BookInfo.objects.get(id=6)
book.name = '开发入门'
book.save()
# 方式二 filter过滤,update更改
BookInfo.objects.filter(id=6).update(name='方式二修改',commentcount=66)

################# 删除 ##########################
# 删除分两种,物理删除(这条记录的数据删除),逻辑删除(修改标记位,例如 is_delete=False),选哪个需要结合需求
#方式一:
book = BookInfo.objects.get(id=6)
book.delete()  # 物理删除,这里的是ORM中的delete命令,他会自己转化为mysql语句去执行

# 方式二:
BookInfo.objects.get(id=6).delete()
BookInfo.objects.filter(id=6).delete()

######################## 查询 #########################
try:
    book = BookInfo.objects.get(id=1)  # 查询一个,但是这个有可能不存在,容易出现异常
except BookInfo.DoesNotExist:
    print('查询结果不存在')
BookInfo.objects.all()  # 查询所有

# count 查询结果数量
BookInfo.objects.all().count()
BookInfo.objects.count()

# 过滤查询 filter,get,exclude
# 语法形式: 模型类名.filter(属性名__运算符 = 值)  获取n个结果,从0到n
# 语法形式: 模型类名.exclude(属性名__运算符 = 值)  获取n个结果,从0到n
# 语法形式: 模型类名.get(属性名__运算符 = 值)  获取1个结果 或者 异常

# 查询编号为1的图书
book = BookInfo.objects.get(id = 1)            # 简写形式  (属性名=值)
book = BookInfo.objects.get(id_exact = 1)      # 完整形式

book = BookInfo.objects.get(pk = 1)    # pk表示主键 primary key

# 查询书名中包含'湖'的图书
BookInfo.objects.filter(name__contains='湖')
# 查询编号为1或3或5的图书
BookInfo.objects.filter(id__in=[1,3,5])
# 查询编号不等于3的图书
BookInfo.objects.exclude(id=3)
# 日期匹配格式 1991-1-1

##################################################3
from django.db.models import F
# 两个属性的比较
# 阅读量大于 评论量的读书
BookInfo.objects.filter(readcount__gt=F('commentcount'))  # F('commentcount')可以做数学运算

##并且查询
# 阅读量大于20且编号小于3的图书,下面两种方式都可以
BookInfo.objects.filter(readcount__gt=20,id__lt=3)
BookInfo.objects.filter(readcount__gt=20).filter(id__lt=3)
# 或者查询
from django.db.models import Q
# 语法:模型类名.objects.filter(Q(属性名__运算符 = 值) | Q(属性名__运算符 = 值) |.....)
BookInfo.objects.filter(Q(readcount__gt=20)|Q(id__lt=3))

# Q还可以实现 非 语法    BookInfo.objects.filter(~Q(属性名__运算符 = 值))