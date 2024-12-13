from tkinter.constants import CASCADE

from django.db import models


# Create your models here.
class Admin(models.Model):

     username = models.CharField(verbose_name="账户名", max_length=50)
     password = models.CharField(verbose_name="密码", max_length=50)

     def __str__(self):
         return self.username



class Department(models.Model):
    department_name = models.CharField(verbose_name="部门名称",max_length=50)

    def __str__(self):
        return self.department_name


class UserInfo(models.Model):
    name = models.CharField(max_length=50,verbose_name="姓名")
    password = models.CharField(max_length=50,verbose_name="密码")
    age = models.IntegerField(verbose_name="年龄")

    account = models.DecimalField(default=0, verbose_name='账户余额', max_digits=10, decimal_places=2)
    # create_time = models.DateTimeField(verbose_name="入职时间")
    create_time = models.DateField(verbose_name="入职时间")

    depart = models.ForeignKey(to="Department", to_field="id", on_delete=models.CASCADE, verbose_name='部门')

    gender_choices = (
        (1,'男'),
        (2,'女'),
    )

    gender = models.IntegerField(choices=gender_choices, verbose_name='性别')


class PrettyNum(models.Model):
    mobile = models.CharField(verbose_name='号码', max_length=50)
    price = models.DecimalField(verbose_name='价格', max_digits=10, decimal_places=2)

    level_choice = (
        (1,'1级'),
        (2,'2级'),
        (3,'3级'),
        (4,'4级'),
        (5,'5级'),
    )
    level = models.SmallIntegerField(verbose_name='等级', choices=level_choice, default=1)

    price_choice = (
        (1, '已占用'),
        (2, '未占用'),
    )
    status = models.SmallIntegerField(verbose_name='状态', choices=price_choice, default=2)


class TaskInfo(models.Model):
    level_choice = (
        (1,'紧急'),
        (2,'重要'),
        (3,'临时'),
    )

    level = models.SmallIntegerField(verbose_name='级别',choices=level_choice,default=1)
    title = models.CharField(verbose_name='标题', max_length=64)
    detail = models.TextField(verbose_name='详情')
    user = models.ForeignKey(verbose_name='负责人', to=Admin, on_delete=models.CASCADE)


class Boss(models.Model):
    name= models.CharField(max_length=64 ,verbose_name='名字')
    age= models.IntegerField(verbose_name='年龄')
    img= models.CharField(max_length=128,verbose_name='头像')


class City(models.Model):
    name= models.CharField(max_length=32 ,verbose_name='城市名')
    count= models.IntegerField(verbose_name='人口')
    img= models.FileField(max_length=128,verbose_name='logo',upload_to='city/')

