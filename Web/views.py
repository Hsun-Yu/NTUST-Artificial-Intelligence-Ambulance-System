from django.http import HttpResponse
from django.shortcuts import render, redirect
#from newsadmapp import models
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
#from django.views.decorators.csrf import ensure_csrf_cookie
from django import template
import math
#form ambulance_system import Location

# Create your views here.

def home(request):
	latitude = 25.0068
	longitude = 121.5233
	return render(request,"home.html",locals())

def sign(request):
	messages = ''  #初始時清除訊息
	if request.method == 'POST':  #如果是以POST方式才處理
		name = request.POST['username'].strip()  #取得輸入帳號
		password = request.POST['password']  #取得輸入密碼

		user1 = authenticate(username=name, password=password)  #驗證
		if user1 is not None:  #驗證通過
			if user1.is_active:  #帳號有效
				auth.login(request, user1)  #登入
				return redirect('/adminmain/')  #開啟管理頁面
			else:  #帳號無效
				messages = '帳號尚未啟用！'
		else:  #驗證未通過
			messages = '登入失敗！'
#		if name=='jame':
#			if  password == '123':
#				return redirect('/adminmain/')
#			else:
#				messages = 'wrong password'
#		else:
#			messages = 'wrong uwer name'
	return render(request,"sign.html",locals())

def adminmain(request):
	return HttpResponse("welcome")
	return render(request,"adminmain.html",locals())

def index(request):

	return render(request,"index.html",locals())

def schedule(request):

	begin_latitude = 25.0068
	begin_longitude = 121.5233
	finish_latitude = 24.1234
	finish_longitude = 120.4321

	return render(request,"schedule.html",locals())