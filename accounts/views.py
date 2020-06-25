from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login
from accounts.forms import SignUpForm
from django.contrib.auth.decorators import login_required

from django.contrib import messages

# def Login(request):
# 	import pdb; 
# 	pdb.set_trace()

# 	if request.method == "POST":

# 		username = request.POST["username"]
# 		password = request.POST["password"]

# 		user=authenticate(username=username,password=password)
# 		if user is not None:
# 			login(request,user)
# 			return redirect("/")
# 	else:
# 		messages.error(request,"user invalid")
# 		return render(request,"accounts/login.html",{})



# def SignUp(request):
# 	if request.method == "POST":
# 		form = SignUpForm(request.POST)
# 		if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('/')
#     else:
#         form = SignUpForm()
#     return render(request, 'login.html', {'form': form})
@login_required
def home(request):
    return render(request, '../home/templates/Home/homepage.html')


def SignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        import pdb;
        pdb.set_trace()
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/login.html', {'form': form})





# username= request.POST["username"]
		# email=request.POST['email']
		# first_name=request.POST["first_name"]
		# password = request.POST["password"]
		# #password = request.POST["password2"]
		
		#login(request, user)

	# 	if password1==password2:
	# 		if User.objects.filter(username=username).exists():
	# 			messages.info(request,'Username taken')
	# 			return redirect("signup")
	# 		elif User.objects.filter(email=email).exists():
	# 			messages.info(request,'email taken')
	# 			return redirect("signup")
	# 		else:
	# 			user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name)
	# 			user.save()
	# 			return redirect("signup")
	# 	else:
	# 		messages.info(request,"Your Password Doesn't Match")
	# 		return redirect("signup")
	# 	return redirect("/")
	# else:	
	# 	return render(request,"accounts/login.html",{})

	
		