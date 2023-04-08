from django.db import models

class Picture(models.Model):
    car_number = models.CharField(max_length=50,blank=True,null=True)
    status = models.BooleanField(default=True,blank=True,null=True)
    started_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return self.car_number
    