from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token_generator import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

# Create your views here.
from .models import *
from .forms import  CreateUserForm
from django.contrib.auth import views



def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
            	user = form.save(commit=False)
            	user.is_active = False
            	user.save()
            	current_site = get_current_site(request)
            	email_subject = 'Activate Your Account'
            	message = render_to_string('accounts/activate_account.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
                 })
            	to_email = form.cleaned_data.get('email')
            	email = EmailMessage(email_subject, message, to=[to_email])
            	email.send()
            	messages.success(request, 'Confirm your email to complete the registration')
            	return redirect('login')
        context = {'form':form}
        return render(request, 'accounts/signup.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user,backend='django.contrib.auth.backends.ModelBackend')
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)
def activate_account(request, uidb64, token, backend='django.contrib.auth.backends.ModelBackend'):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except (TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		# user.profile.email_confirmed = True
		user.save()
		auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
		return redirect('home')
	else:
		return HttpResponse("invalid mail")
@login_required
def logout(request):
    auth_logout(request)
    return redirect('home')


