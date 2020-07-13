from django.db import models

# Create your models here.
class booking(models.Model):
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


