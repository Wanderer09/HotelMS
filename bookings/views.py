from django.shortcuts import render,redirect
from .models import booking

# Create your views here.
def bookings(request):
	if(request.method=='GET'):
		in_date=request.GET.get('in_date','')
		in_time=request.GET.get('in_time','')
		out_date=request.GET.get('out_date','')
		out_time=request.GET.get('out_time','')
		room_count=request.GET.get('room_count','')
		guest_count=request.GET.get('guest_count','')
		adult_count=request.GET.get('adult_count','')
		children_count=request.GET.get('children_count','')
		country=request.GET.get('country','')
		fname=request.GET.get('fname','')
		lname=request.GET.get('lname','')
		phonenumber=request.GET.get('phonenumber','')
		town=request.GET.get('town','')
		gender=request.GET.get('gender','')
		email=request.GET.get('email','')
		identification=request.GET.get('identification','')
		booking1=booking(in_date=in_date,in_time=in_time,out_date=out_date,out_time=out_time,room_count=room_count,guest_count=guest_count,adult_count=adult_count,children_count=children_count,country=country,fname=fname,lname=lname,phonenumber=phonenumber,town=town,gender=gender,email=email,identification=identification)
		booking1.save()
		return redirect('booking2')
	return render(request,'bookings/booking.html',{})
def booking2(request):
    return render(request,'bookings/booking2.html')
def booking3(request):
    return render(request,'bookings/booking3.html')
def booking4(request):
    return render(request,'bookings/booking4.html')
