from django.db import models
from utils.models import City
# Create your models here.

class TimeSlots(models.Model):
    timming                 =     models.CharField(max_length=120)


    def __str__(self):
        return self.timming

class AppointmentBooking(models.Model):
    # user                    =       models.ForeignKey(User,on_delete=models.CASCADE)
    name                    =       models.CharField(max_length=120)
    phone                   =       models.CharField(max_length=120)
    email                   =       models.EmailField(unique=True)
    appointment_date        =       models.DateField()
    time_slot               =       models.ForeignKey(TimeSlots,on_delete=models.SET_NULL,blank=True,null=True)
    address_line_1          =       models.CharField(max_length=500)
    address_line_2          =       models.CharField(max_length=500)
    landmark                =       models.CharField(max_length=500)
    city                    =       models.ForeignKey(City,on_delete=models.SET_NULL,blank=True,null=True)


    def __str__(self):
        return self.name
