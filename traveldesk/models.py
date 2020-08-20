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
class pick_drop(models.Model):
	name=models.CharField(max_length=100)
	room_number=models.CharField(max_length=100)
	contact=models.CharField(max_length=100)
	email=models.CharField(max_length=100,default='')
	pick_location=models.CharField(max_length=100,default='')
	drop_location=models.CharField(max_length=100,default='')
	time=models.CharField(max_length=100,default='')
	driver=models.CharField(max_length=100,default='None')
	vehicle_category=models.CharField(max_length=100,default='prime_car')
	registered_number=models.CharField(max_length=100,default='None')
	status=models.CharField(max_length=100,default='unclear')


