from django.shortcuts import render

# Create your views here.
def bookings(request):
    return render(request,'bookings/booking.html',{})
def booking2(request):
    return render(request,'bookings/booking2.html')