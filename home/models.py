from django.db import models

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    date=models.DateField(auto_now=True)
    time=models.TimeField(auto_now=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")
    status=models.CharField(max_length=100,default='cleared')


    def __str__(self):
        return self.name
class Restaurant_Booking(models.Model):
	name=models.CharField(max_length=50)
	phonenumber=models.CharField(max_length=50)
	Number_of_persons=models.PositiveIntegerField()
	date=models.DateField(auto_now=False,auto_now_add=False)
	time=models.TimeField(auto_now=False,auto_now_add=False)

