#coding:utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse
from login.models import *
from django.http import HttpResponseRedirect

# Create your views here.
def valid_login(func):
	def inner(request,*args,**kwargs):
		if request.session.get("username",""):
			username = request.session.get(username)
			if username:
				userData = User.objects.get(user = username)
				all_dict = {
					"user":userData,
					"passwd":userData.passwd,
					"name":userData.name,
					"city":userData.city,
					"email":userData.email,
					"phone":models.phone,
				}
				request.session["UserData"] = all_dict
				return func(request)
		else:
			print 'aaaa'
			return render(request,'index.html')
	return inner

@valid_login
def  index(request):
	username = request.COOKIES.get("user","")
	print username 
	# return render(request,'index.html')
	# if request.session.get("username",""):
	# 	return render(request,'index.html',{"username":username})
	# else:
	return render(request,'signin.html')
	# return render(request,'index.html',{"username":username})

def userValid(username):
	userlist = User.objects.filter(user = username)#select * from Users where user = username
	if userlist:
		# return {"passwd":userlist[0].passwd}
		return True
	else:
		return False

def signin(request):
	print request.method
	if request.method == "POST" and request.POST:
		user = request.POST["user"]
		password = request.POST["password"] 
		if userValid(user):
			data = User.objects.get(user = user)  #获取user 字段等于user的信息
			passwd = data.passwd
			if passwd == password: #验证密码正确与否
				#设置cookie 和session 验证 都是用来作为用户登入身份验证的一部分，区别在于 cookie保存在浏览器
				#而session保存在服务器端， cookie 和 session 都可以被服务器下一个请求读到，但是session 更安全
				# response = HttpResponseRedirect('index.html')#实例化一个response相应
				response = render(request,"index.html")
				response.set_cookie("user",user) #cookie 对该相应设置cookie
				request.session['userdata'] = user #设置sesssion
				# if request.session["userdata"]:
				# 	return response
				# else:
				# 	return render(request,'index.html')
				#正常情况应该跳转到index 视图
				return response
			else:
				# return HttpresponseRedirect("/signin")
				return render(request,'signin.html')
		else:#如果请求方式不对或者请求方式为空
			# return HttpresponseRedirect("/signin")
			return render(request,'signin.html')
	else:
	# return render(request,'signin.html')
		return render(request,'signin.html')
		# return render(request,'index.html')


def signup(request):
	if request.method == "POST" and request.POST:
		u = User()
		# u.user = request.POST("user")
		# u.passwd = request.POST("passwd")
		# u.name = request.POST("name")
		# u.city = request.POST("city")
		# u.email = request.POST("email")
		# u.phone = request.POST("phone")
		u.user = request.POST["user"]
		u.passwd = request.POST["passwd"]
		u.name = request.POST["name"]
		u.city = request.POST["city"]
		u.email = request.POST["email"]
		u.phone = request.POST["phone"]
		u.save()
		return render(request,'signin.html')
	else:
		return render(request,'signup.html')

def serverRegister(request):
	# if request.method == "POST" and request.POST:
	# 	s = Server()
	# 	s.hostname = request.POST["HostName"]
	# 	s.ip = request.POST["Ip"]
	# 	s.Mac = request.POST["MAC"]
	# 	s.cpu = request.POST["CPU"]
	# 	s.cpu = request.POST["MEM"]
	# 	s.cpu = request.POST["DISK"]
	# 	s.cpu = request.POST["System"]
	# 	s.cpu = request.POST["IO"]
	return render(request,'serverRegister.html')