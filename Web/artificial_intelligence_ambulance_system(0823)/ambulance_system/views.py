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
import json

# Register your models here.
#from ambulance_system.models import TrafficConditionLog
from ambulance_system.models import TrafficConditionLog,Monitor,Location,ResponsibleUnit,TrafficCondition,Ambulance,AmbulanceSchedule
# Create your views here.


global search
search=2
global location_name2
location_name2=""


def adminmain_home(request):
	global search
	search=0

	if request.user is not None:  #驗證通過
		if request.user.is_active:  #帳號有效
			return redirect('/adminmain/')  #開啟管理頁面
		else:  #帳號無效
				messages = '帳號尚未啟用！'
				return redirect('/index/')
	else:  #驗證未通過
			messages = '登入失敗！'
			return redirect('/index/')


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
	



	global search

	global location_name2
	location_name=""

	if search == 1:

		if request.method == 'POST':
			location_name = request.POST['location_name']  # 從前台抓取資料(路段名)

			if location_name != "":
				location_name2 = location_name

		locations = Location.objects.filter(Name__contains=location_name2)
		monitors = Monitor.objects.filter(Location__in=locations)
		car_accidents = TrafficConditionLog.objects.filter(Monitor__in=monitors)

		locations = Location.objects.filter(CountryName__contains=location_name2)
		monitors = Monitor.objects.filter(Location__in=locations)
		car_accidents_all = TrafficConditionLog.objects.filter(Monitor__in=monitors)
		name = "路段為" + location_name2
		name2 = "地區為" + location_name2
		search = 1
	elif request.method == 'POST':
		location_name = request.POST['location_name']  # 從前台抓取資料(路段名)
		location_name2 = location_name

		locations = Location.objects.filter(Name__contains=location_name)
		monitors = Monitor.objects.filter(Location__in=locations)
		car_accidents = TrafficConditionLog.objects.filter(Monitor__in=monitors)

		locations = Location.objects.filter(CountryName__contains=location_name)
		monitors = Monitor.objects.filter(Location__in=locations)
		car_accidents_all = TrafficConditionLog.objects.filter(Monitor__in=monitors)
		name = "路段為" + location_name
		name2 = "地區為" + location_name
		search = 1
	else:
		Unit = ResponsibleUnit.objects.filter(Name=request.user.username)
		car_accidents = TrafficConditionLog.objects.filter(ResponsibleUnit__in=Unit)
		car_accidents_all = TrafficConditionLog.objects.all().order_by('Monitor')
		name = request.user.username
		name2 = "系統"
		search = 0

	if request.user is not None:  #驗證通過
		if request.user.is_active:  #帳號有效
			return render(request,"adminaa.html",locals())  #開啟管理頁面
		else:  #帳號無效
				messages = '帳號尚未啟用！'
				return redirect('/index/')
	else:  #驗證未通過
			messages = '登入失敗！'
			return redirect('/index/')


	return render(request,"adminaa.html",locals())


def index(request):

	search=2
	location_name2=""
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

	# begin_latitude = car_accident.ResponsibleUnit.Location.Latitude
	# begin_longitude = car_accident.ResponsibleUnit.Location.Longitude
	# finish_latitude = car_accident.Monitor.Location.Latitude
	# finish_longitude = car_accident.Monitor.Location.Longitude

#	begin_latitude = 25.0068
#	begin_longitude = 121.5233
#	finish_latitude = 25.1234
#	finish_longitude = 121.4321
	# start = str(begin_latitude)+','+str(begin_longitude)
	# end = str(finish_latitude)+','+str(finish_longitude)
#	start='25,121'
#	end='26.3,121'

	context = {
		'caraccident':car_accident,
    }
	return render(request,'schedule.html', context)

def logout(request):
	django_logout(request)
	return redirect('/index/')  #開啟管理頁面


def check(request,id):


	car_accident = TrafficConditionLog.objects.get(id=id)
	if car_accident.ResponsibleUnit.Name==request.user.username:
		
		if car_accident.Processed == True:
			car_accident.Processed = False
		else :
			car_accident.Processed = True
		car_accident.save()
	else :
		return HttpResponse("您沒有權限更改此資料")
		


	return redirect('/adminmain/')


def finish(request):

	car_accidents=TrafficConditionLog.objects.filter(Solved=True)

	return render(request, "adminff.html", locals())



def table(request):
	if request.method == 'POST':
		location_name=request.POST['location_name']#從前台抓取資料(路段名)
		location=Location.objects.get(Name__contains=location_name)
		monitor=Monitor.objects.get(Location=location)

		time=request.POST['time']
		
		size=request.POST['size']
		condition=TrafficCondition.objects.get(Name__contains=size)

		process=request.POST['process']

		unit_name=request.user.username
		unit=ResponsibleUnit.objects.get(Name__contains=unit_name)

		log=TrafficConditionLog.objects.create(Monitor=monitor, TrafficCondition=condition, Datetime=time, ResponsibleUnit=unit, Solved=False, Processed=process)
		log.save()
	return render(request, "admintable.html", locals())







def editdata(request,id):
	car_accident=TrafficConditionLog.objects.get(id=id)

	if request.method == 'POST':
		unit_name=request.POST['unit_name']
		unit=ResponsibleUnit.objects.get(Name__contains=unit_name)
		car_accident.ResponsibleUnit=unit

		car_accident.TrafficCondition.Name=request.POST['unit_name']
		car_accident.Processed=request.POST['process']
		car_accident.Solved=request.POST['solved']
		car_accident.save()
		return redirect('/adminmain/')


	return render(request, "editdata.html", locals())