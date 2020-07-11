from django.shortcuts import render

# Create your views here.
def bookings(request):
	# if request.method=='POST':
	# 	in_date=request.POST['in_date']
	# 	# in_time=request.POST['in_time']
	# 	# out_date=request.POST['out_date']
	# 	# out_time=request.POST['out_time']
	# 	# room_count=request.POST['room_count']
	# 	# guest_count=request.POST['guest_count']
	# 	# adult_count=request.POST['adult_count']
	# 	# children_count=request.POST['children_count']
	# 	# country=request.POST['country']
	# 	# fname=request.POST['fname']
	# 	# lname=request.POST['lname']
	# 	# phonenumber=request.POST['phonenumber']
	# 	# town=request.POST['town']
	# 	# gender=request.POST['gender']
	# 	# email=request.POST['email']
	# 	# identification=request.POST['identification']
    return render(request,'bookings/booking.html',{})
def booking2(request):
    return render(request,'bookings/booking2.html')
def booking3(request):
    return render(request,'bookings/booking3.html')
