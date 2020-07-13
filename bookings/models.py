from django.db import models

# Create your models here.
class booking(models.Model):
	in_date=models.DateField(blank=False)
	in_time=models.TimeField(blank=False,auto_now=False, auto_now_add=False)
	out_date=models.DateField(blank=False)
	out_time=models.TimeField(blank=False,auto_now=False, auto_now_add=False)
	room_count=models.PositiveIntegerField(blank=False)
	guest_count=models.PositiveIntegerField(blank=False)
	adult_count=models.PositiveIntegerField(blank=False)
	children_count=models.PositiveIntegerField(blank=False)
	country=models.CharField(blank=False,max_length=100)
	fname=models.CharField(blank=False,max_length=50)
	lname=models.CharField(blank=False,max_length=50)
	phonenumber=models.CharField(blank=False,max_length=50)
	town=models.CharField(blank=False,max_length=50)
	gender=models.CharField(blank=False,max_length=10)
	email=models.CharField(blank=False,max_length=50)
	identification=models.CharField(blank=False,max_length=50)


