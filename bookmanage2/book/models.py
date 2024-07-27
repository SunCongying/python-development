from django.db import models

# Create your models here.

##书籍列表信息的模型类
class BookInfo(models.Model):
    # 创建字段，字段类型
    name = models.CharField(max_length=20,verbose_name='名称')
    pub_date = models.DateField(verbose_name='发布日期',null=True)
    readcount = models.IntegerField(default=0,verbose_name='阅读量')
    commentcount = models.IntegerField(default=0,verbose_name='评论量')
    is_delete = models.BooleanField(default=False,verbose_name='逻辑删除')
    # 逻辑删除不是真正的删除了数据，而是用is_delete作为标记表示记录已被删除，可以保留数据的完整性。

    # Meta类用于定义模型的元数据（metadata），即与模型本身相关的配置和选项
    class Meta:
        db_table = 'bookinfo'  # # 指定数据库中表的名称,Django中的默认表名是：模型的小写形式，
        verbose_name = '图书'  # 定义模型的可读名称，通常用于Django管理界面中显示。

    def __str__(self):
        # 定义每个数据对象的显示信息
        return self.name

# 人物表
class PeopleInfo(models.Model):
    GENDER_CHOICE = (
        (0,'male'),
        (1,'female')
    )

    name = models.CharField(max_length=10,verbose_name='名称')
    gender = models.SmallIntegerField(choices=GENDER_CHOICE,default=0,verbose_name='性别')
    description = models.CharField(max_length=20,null=False,verbose_name='描述信息')
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE,verbose_name='图书')
    is_delete = models.BooleanField(default=False,verbose_name='逻辑删除')

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物信息'

    def __str__(self):
        return self.name

