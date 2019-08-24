from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import logout as django_logout
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from django import template
import math
from django.utils.datastructures import MultiValueDictKeyError

# Register your models here.
#from ambulance_system.models import TrafficConditionLog
from ambulance_system.models import TrafficConditionLog,Monitor,Location,ResponsibleUnit,TrafficCondition,Ambulance,AmbulanceSchedule
# Create your views here.

def home(request):
	return redirect('/index/')  #開啟管理頁面

def sign(request):
	messages = ''  #初始時清除訊息
	if request.method == 'POST':  #如果是以POST方式才處理
		name = request.POST['username'].strip()  #取得輸入帳號
		password = request.POST['password']  #取得輸入密碼

		user1 = authenticate(username=name, password=password)  #驗證
		if user1 is not None:  #驗證通過
			if user1.is_active:  #帳號有效
				auth.login(request, user1)  #登入
				return redirect('/index/')  #開啟管理頁面
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
	return render(request,"index.html",locals())

def adminmain(request):
	return HttpResponse("welcome")
	return render(request,"adminmain.html",locals())

def index(request):

	#搜尋部分
	if request.method == 'POST':
		location_name=request.POST['location_name']#從前台抓取資料(路段名)
		location_country=request.POST['location_country']#從前台抓取資料(地段名)
	#	monitors=Monitor.objects.filter(location_name=Location.values('Name'))
	#	car_accidents = TrafficConditionLog.objects.filter(location_name=Monitor.values('Location'). values ('Name'))
	#	Locations=Location.Get(Name=location_name)
		return render(request, "search.html", locals())
		

	#首頁的顯示
	car_accidents_time=TrafficConditionLog.objects.all().order_by('Datetime')
	car_accidents_size=TrafficConditionLog.objects.all().order_by('-TrafficCondition')
	car_accidents_location=TrafficConditionLog.objects.all().order_by('Monitor')

	return render(request,"index.html",locals())

def schedule(request):

	begin_latitude = 25.0068
	begin_longitude = 121.5233
	finish_latitude = 25.1234
	finish_longitude = 121.4321

	return render(request,"schedule.html",locals())

def logout(request):
	django_logout(request)
	return redirect('/index/')  #開啟管理頁面
	#return render(request,"index.html",locals())

def search(request):


	
	#	car_accidents = TrafficConditionLog.Monitor.Location.objects.filter(name__contains=location_name)
	return HttpResponse("welcome")	
#	return render(request, "search.html", locals())





#	if request.method == 'POST':
#		try:
#			location_name=request.POST['location_name']
#		except MultiValueDictKeyError:
#			location_name=" "
#		try:
#			location_country=request.POST['location_country']
#		except MultiValueDictKeyError:
#			location_country=" "
#		return HttpResponse("welcome"+location_name+location_country)
