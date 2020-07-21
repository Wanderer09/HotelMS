from django.db import models
from django.contrib.auth import get_user_model
user = get_user_model()


# Create your models here.
class booking_guest_details(models.Model):
	user = models.ForeignKey(user, on_delete=models.CASCADE,default='')
	in_date=models.CharField(blank=False,max_length=30)
	in_time=models.CharField(blank=False,max_length=30)
	out_date=models.CharField(blank=False,max_length=30)
	out_time=models.CharField(blank=False,max_length=30)
	room_count=models.CharField(blank=False,default=1,max_length=10)
	guest_count=models.CharField(blank=False,default=1,max_length=10)
	adult_count=models.CharField(blank=False,default=1,max_length=20)
	children_count=models.CharField(blank=False,default=1,max_length=10)
	country=models.CharField(blank=False,max_length=100,default='India')
	fname=models.CharField(blank=False,max_length=50)
	lname=models.CharField(blank=False,max_length=50)
	phonenumber=models.CharField(blank=False,max_length=50)
	town=models.CharField(blank=False,max_length=50)
	gender=models.CharField(blank=False,max_length=10)
	email=models.CharField(blank=False,max_length=50)
	identification=models.CharField(blank=False,max_length=50)
class booking_room_details(models.Model):
	booking_guest_details=models.ForeignKey(booking_guest_details, on_delete=models.CASCADE)
	user = models.ForeignKey(user, on_delete=models.CASCADE)
	Room_details=models.TextField()
	service_details=models.TextField()
	amount=models.CharField(max_length=10)
	payment_type=models.CharField(max_length=20,blank=False)
	payment_status=models.CharField(max_length=30,blank=False)
	booking_status=models.CharField(max_length=20,blank=False)
class booking(models.Model):
	user = models.ForeignKey(user, on_delete=models.CASCADE)
	made_on = models.DateTimeField(auto_now_add=True)
	amount = models.IntegerField()
	booking_guest_details=models.ForeignKey(booking_guest_details,on_delete=models.CASCADE)
	booking_room_details=models.ForeignKey(booking_room_details,on_delete=models.CASCADE)




