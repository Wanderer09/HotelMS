from django.shortcuts import render

# Create your views here.
def restro_manager(request):
	return render(request,'manager/restro_manager.html',{})