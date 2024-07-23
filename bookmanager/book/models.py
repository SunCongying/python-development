from django.db import models

# Create your models here.
"""
1.我们的模型类需要继承自models.Model
2.系统会为我们自动添加一个主键--id
3.字段
    字段名=model.类型（选项），就是数据表中的字段名，不要使用python，mysql等关键字
4.表的名称，默认是：子应用名_类名 都是小写，可以通过Meta函数，db_table=‘’修改。这是django官方默认的
decimal是货币类型，只要是钱就使用该类型
"""
'''
先创建ORM类，再通过迁移生成表
实际项目中也有根据表生成类的。只需要生成迁移文件，不需要执行迁移

'''

#### 书籍表 ####
class BookInfo(models.Model): # 表对应的类，需要先注册，再进行模型迁移才能完成建表
    # 创建字段
    name = models.CharField(max_length=10,unique=True)
    pub_date = models.DateField(null=True)
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)
    # 修改表的名称
    class Meta:
        db_table = 'bookinfo'
        verbose_name = '书籍管理' # admin站点使用的

    # 重写str方法，使得显示书籍名称
    def __str__(self):
        return self.name  # 该表的内容是id，name，所以这里返回self.name
####人物表 ###
class PeopleInfo(models.Model):

    # 定义一个有序字典存储性别
    GENDER_CHOICE = (
        (1,'male'),
        (2,'female')
    )

    name=models.CharField(max_length=10,unique=True) # unique表示唯一
    gender=models.SmallIntegerField(choices=GENDER_CHOICE,default=1)
    description = models.CharField(max_length=100,null=True)
    is_delete = models.BooleanField(default=False)

    # 外键约束,系统会自动为外键添加 _id,可以直接命名名字：book
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)
    # BookInfo：外键对应的类名
    # on_delete 表示主表删除数据时，外键引用的数据该如何处理
    # 主表 从表
    #  1 对 多 的关系 书籍对人物
    # SET_NULL ：仅在字段null=True时，将外键引用的数据变为null
    # SET():将外键引用的数据变为特定值或调用特定方法
    # CASCADE： 级联操作，连同外键表中的数据一起删除
    # protect：保护，阻止删除主表中外键使用的数据

    class Meta:
        db_table = 'peopleinfo'

# 每次修改了模型文件中的类，就要生成一个迁移文件。


