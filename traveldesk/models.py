from django.db import models

# Create your models here.
class vehicle(models.Model):
	vehicle=models.CharField(max_length=100)
	vehicle_name=models.CharField(max_length=100)
	registered_number=models.CharField(max_length=100)
	vehicle_category=models.CharField(max_length=100)
	vehicle_status=models.CharField(max_length=100)
class driver_details(models.Model):
	driver_name=models.CharField(max_length=100)
	driver_phonenumber=models.CharField(max_length=20)
	driver_gender=models.CharField(max_length=10)
	driver_age=models.PositiveIntegerField()
	driver_status=models.CharField(max_length=20)
	vehicle_alloted=models.CharField(max_length=20)
	number=models.CharField(max_length=20)
	vehicle_number=models.ForeignKey(vehicle,on_delete=models.CASCADE,to_field='id')
class vehicle_bookings(models.Model):
	guest_name=models.CharField(max_length=100)
	room_number=models.CharField(max_length=100)
	vehicle=models.CharField(max_length=100)
	vehicle_type=models.CharField(max_length=100)
	vehicle_number=models.CharField(max_length=100)
	driver_type=models.CharField(max_length=100)
	driver_alloted=models.CharField(max_length=100)
	time_alloted=models.CharField(max_length=100)
	made_on = models.DateTimeField(auto_now_add=True)


