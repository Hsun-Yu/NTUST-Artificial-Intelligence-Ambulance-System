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
	global user1
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

	return render(request,"index.html",locals())



def adminmain(request):
	global user1


	user=user1

	Unit=ResponsibleUnit.objects.filter(Name=user.username)
	car_accidents = TrafficConditionLog.objects.filter(ResponsibleUnit__in=Unit)



	return render(request,"adminmain.html",locals())


def index(request):

	#搜尋部分
	if request.method == 'POST':
		location_name=request.POST['location_name']#從前台抓取資料(路段名)
		location_country=request.POST['location_country']#從前台抓取資料(地段名)

		if location_name == "":
			locations=Location.objects.filter(CountryName__contains=location_country)
			monitors=Monitor.objects.filter(Location__in=locations)
			car_accidents = TrafficConditionLog.objects.filter(Monitor__in=monitors)
		else:
			locations=Location.objects.filter(Name__contains=location_name)
			monitors=Monitor.objects.filter(Location__in=locations)
			car_accidents = TrafficConditionLog.objects.filter(Monitor__in=monitors)
		return render(request, "search.html", locals())
		

	#首頁的顯示
	car_accidents_time=TrafficConditionLog.objects.all().order_by('Datetime')
	car_accidents_size=TrafficConditionLog.objects.all().order_by('-TrafficCondition')
	car_accidents_location=TrafficConditionLog.objects.all().order_by('Monitor')

	return render(request,"index.html",locals())

def schedule(request,id):

	car_accident=TrafficConditionLog.objects.get(id=id)
	
	begin_latitude = car_accident.ResponsibleUnit.Location.Latitude
	begin_longitude = car_accident.ResponsibleUnit.Location.Longitude
	finish_latitude = car_accident.Monitor.Location.Latitude
	finish_longitude = car_accident.Monitor.Location.Longitude

	#return render(request,"home.html",locals())
	return render(request,"schedule.html",locals())

def logout(request):
	django_logout(request)
	return redirect('/index/')  #開啟管理頁面

