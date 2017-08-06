#coding:utf-8
from django.db import models

# Create your models here.
class BaseModel(models.Model):
	delete_flag = models.CharField(max_length = 4, verbose_name = "删除标志")


class User(models.Model):
	user = models.CharField(max_length = 32,verbose_name = "登入名")
	passwd = models.CharField(max_length = 32)
	name = models.CharField(max_length = 32)
	city = models.CharField(max_length = 32)
	email = models.CharField(max_length = 64)
	phone = models.CharField(max_length = 32)
	delete_flag = models.CharField(max_length = 4, verbose_name="删除标志")

# select * from User where delete_flag = True

#设置
class Group(BaseModel):
	Name = models.CharField(max_length = 32, verbose_name = "组名")
	description = models.TextField(verbose_name = "组描述")
#权限
class Permission(BaseModel):
	Name = models.CharField(max_length = 32, verbose_name = "权限名称")
	description = models.TextField(verbose_name = "权限描述")
#用户组
class User_Group(BaseModel): 
	userID = models.IntegerField(verbose_name = "用户 id")
	groupID = models.IntegerField(verbose_name = "组 id")

#用户权限
class User_Permission(BaseModel): 
	userID = models.IntegerField(verbose_name = "用户 id")
	groupID = models.IntegerField(verbose_name = "组 id")

#主页信息展示，收集集群的信息。
class Server(BaseModel):
	Hostname = models.CharField(max_length = 32,verbose_name="主机名")
	Mac = models.CharField(max_length = 32,verbose_name="物理地址")
	Ip = models.CharField(max_length = 32,verbose_name="IP")
	Cpu = models.CharField(max_length = 32,verbose_name="cpu")
	Mem = models.CharField(max_length = 32,verbose_name="内存")
	Disk = models.CharField(max_length = 32,verbose_name="磁盘")
	IO = models.CharField(max_length = 32,verbose_name="读写")
	LastLogin = models.DateTimeField(max_length = 32,verbose_name="上次登入时间")
	LastLoginUser = models.CharField(max_length = 32,verbose_name="上次登入的用户")
	isActive = models.CharField(max_length = 32,verbose_name="是否被激活")

class UserServer(BaseModel):
	userID = models.IntegerField()
	serId = models.IntegerField()




# class User_Group(BaseModel): 
# 	userID = models.IntegerField(verbose_name = "用户 id")
# 	groupID = models.IntegerField(verbose_name = "组 id")


