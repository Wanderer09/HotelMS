from django.db import models
# Create your models here.
class Customer_Account(models.Model):
	Full_Name=models.CharField(max_length=30);
	Email=models.EmailField(max_length=50,unique=True,db_index=True)
	PhoneNumber=models.IntegerField(default=0)
	Password=models.CharField(max_length=20)
	Confirmation_Status=models.BooleanField(default=False)
	# Customer_Login_id=models.ForeignKey('Customer_Login',on_delete=models.CASCADE)
# class Customer_Login(models.Model):
# 	Email=models.EmailField(max_length=100,unique=True,db_index=True)
# 	Password=models.CharField(max_length=100)
# 	Customer_Signup_id=models.ForeignKey('Customer_Signup',on_delete=models.CASCADE)