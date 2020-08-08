from django.shortcuts import render

# Create your views here.
def traveldesk_home(request):
	return render(request,'traveldesk/travel.html',{})