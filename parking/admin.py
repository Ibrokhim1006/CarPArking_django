from django.contrib import admin
from parking.models import *


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ('number',)


@admin.register(Parking)
class Parking(admin.ModelAdmin):
    list_display = ('security_name','parking_status','category','camera_ip_adress','author')
    
    
@admin.register(CarInParking)
class CarInParking(admin.ModelAdmin):
    list_display = ('car_number','parking','price','status','started_at')
    search_fields = ('car_number','status','parking')
    
