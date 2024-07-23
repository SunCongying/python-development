from django.db import models

# Create your models here.
"""
1.我们的模型类需要继承自models.Model
2.系统会为我们自动添加一个主键--id
3.字段
    字段名=model.类型（选项），就是数据表中的字段名，不要使用python，mysql等关键字
"""
class BookInfo(models.Model): # 表对应的类，需要先注册，再进行模型迁移才能完成建表
    # 创建字段
    name = models.CharField(max_length=10)

class PeopleInfo(models.Model):
    name=models.CharField(max_length=10)
    gender=models.BooleanField()
    # 外键约束
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)
