from django.db import models
from django.contrib.auth.models import User
import uuid


ParkingStatus = (
    ("KIRISH", "Kirish"),
    ("CHIQISH", "Chiqish")
)

class Category(models.Model):
    number = models.IntegerField(null=False,blank=True)
    slug = models.SlugField(primary_key=True,default=uuid.uuid4,editable=True)
    

class Parking(models.Model):
    security_name = models.CharField(max_length=50,null=False,blank=True)
    parking_status = models.CharField(max_length=10,choices=ParkingStatus,default='KIRISH')
    camera_ip_adress = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete = models.CASCADE,null=True,blank=True)
    created_at = models.DateField(auto_now_add=True)
    slug = models.SlugField(primary_key=True,default=uuid.uuid4,editable=True)
    
    
class CarInParking(models.Model):
    car_number = models.CharField(max_length=50,blank=True,null=True)
    img = models.ImageField(upload_to = 'media/')
    parking = models.ForeignKey(Parking, on_delete=models.CASCADE)
    price = models.FloatField(default=3000,null=True,blank=True)
    status = models.BooleanField(default=True,blank=True,null=True)
    started_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    slug = models.SlugField(primary_key=True,default=uuid.uuid4,editable=True)

    