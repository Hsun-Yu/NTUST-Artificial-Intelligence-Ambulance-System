from django.contrib import admin
from ambulance_system.models import TrafficConditionLog,Monitor,Location,ResponsibleUnit,TrafficCondition,Ambulance,AmbulanceSchedule
# Register your models here.
admin.site.register(Monitor)
admin.site.register(Location)
admin.site.register(ResponsibleUnit)
admin.site.register(TrafficCondition)
admin.site.register(Ambulance)
admin.site.register(AmbulanceSchedule)
admin.site.register(TrafficConditionLog)