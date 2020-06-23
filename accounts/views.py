from django.shortcuts import render,redirect
from .forms import *
from .models import *
# Create your views here.
def login(request):
	login=loginform()
	signup=signupform()
	if(request.method=='POST'):
		login=loginform(request.POST)
		if login.is_valid():
			email=request.POST['Email']
			password=request.POST['Password']
			search=Customer_Account.objects.filter(Email=email,Password=password).exists()
			if(search):
				login=loginform()
				return redirect('home')
			else:
				login=loginform(request.POST)
				return render(request,'accounts/login.html',{'signup_form':signup,'login_form':login})
	return render(request,'accounts/login.html',{'signup_form':signup,'login_form':login})
def signup(request):
	signup=signupform()
	login=loginform()
	if(request.method=='POST'):
		signup=signupform(request.POST)
		if signup.is_valid():
			name=request.POST['Full_Name']
			email=request.POST['Email']
			number=request.POST['PhoneNumber']
			password=request.POST['Password']
			rpassword=request.POST['Retype_Password']
			if(password==rpassword):
				Customer_Account.objects.create(Full_Name=name,Email=email,PhoneNumber=number,Password=password)
				signup=signupform()
				return redirect('home')
		else:
			signup=signupform(request.POST)
			return render(request,'accounts/login.html',{'signup_form':signup,'login_form':login})
	return render(request,'accounts/login.html',{'signup_form':signup,'login_form':login})

