from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage


from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import  CreateUserForm


def SignUp(request):
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
                message = render_to_string('accounts/acc_active_email.html', {
                'user':user, 'domain':current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
                 })
                mail_subject = 'Activate Your Account.'
                to_email = form.cleaned_data.get('email')
                user = form.cleaned_data.get('username')
                email = EmailMessage(mail_subject, message, to=[to_email])
                email.send()
                messages.success(request, 'Account was created for ' + user)
                return HttpResponse('Please confirm your email address to complete the registration.')

                # return redirect('login')
            

        context = {'form':form}
        return render(request, 'accounts/reg.html', context)

def Login(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)

def Logout(request):
    logout(request)
    return redirect('login')
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return render(request,'accounts/login.html')
    else:
        return HttpResponse('Activation link is invalid!')
