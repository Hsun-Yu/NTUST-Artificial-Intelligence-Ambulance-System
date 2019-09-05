from django.db import models

# Create your models here.

class Location(models.Model):
	Name = models.CharField(max_length=255,null=False)
	Latitude = models.FloatField(null=True,blank=True)#緯度
	Longitude = models.FloatField(null=True,blank=True)#精度
	CountryName =models.CharField(max_length=255,null=False)

	def __str__(self):
		return self.Name

class Monitor(models.Model):
	Location = models.ForeignKey(Location,on_delete=models.CASCADE)
	Description = models.TextField(default=False)

	def __str__(self):
		return self.Location.Name

class ResponsibleUnit(models.Model):
	Name = models.CharField(max_length=255,null=False)
	Location = models.ForeignKey(Location,on_delete=models.CASCADE)
	Phone = models.CharField(max_length=15,null=False)

	def __str__(self):
		return self.Name

class TrafficCondition(models.Model):
	Name = models.CharField(max_length=255,null=False)
	DefaultAmbulanceCount = models.IntegerField(default=-1)
	Description = models.TextField(default=False)

	def __str__(self):
		return self.Name

class TrafficConditionLog(models.Model):
	Location = models.ForeignKey(Location,on_delete=models.CASCADE)
	TrafficCondition = models.ForeignKey(TrafficCondition,on_delete=models.CASCADE)
	Datetime = models.DateTimeField(auto_now=True)
	ResponsibleUnit = models.ForeignKey(ResponsibleUnit,on_delete=models.CASCADE)
	Solved = models.BooleanField(default=False)
	Processed = models.BooleanField(default=False)

	def __str__(self):
		return self.Location.Name


class Ambulance(models.Model):
	ResponsibleUnit = models.ForeignKey(ResponsibleUnit,on_delete=models.CASCADE)
	Latitude = models.FloatField(null=True,blank=True)
	Longitude = models.FloatField(null=True,blank=True)
	Status = models.CharField(max_length=20,null=False)

	def __str__(self):
		return self.Status

class AmbulanceSchedule(models.Model):
	Ambulance = models.ForeignKey(Ambulance,on_delete=models.CASCADE)
	TrafficConditionLog = models.ForeignKey(TrafficConditionLog,on_delete=models.CASCADE)
	Status = models.CharField(max_length=20,null=False)

	def __str__(self):
		return self.Status

 










